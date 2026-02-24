"""
โปรแกรม Best-First Search สำหรับหาเส้นทางที่สั้นที่สุดระหว่างเมือง
โดยใช้แผนที่ประเทศโรมาเนีย (Romania Map) เป็นกราฟ
"""

import heapq  # นำเข้าไลบรารี heapq เพื่อใช้จัดการ Priority Queue (คิวลำดับความสำคัญ)
import sys
import io

# แก้ไข encoding สำหรับ Windows ให้แสดงภาษาไทยได้
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


# ==================== คลาสและฟังก์ชันหลัก ====================

# คลาสสำหรับเก็บข้อมูลโหนด (Node) ในการค้นหา
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state          # สถานะ (ชื่อเมือง)
        self.parent = parent        # โหนดพ่อแม่ (โหนดก่อนหน้า)
        self.action = action        # การกระทำที่ทำให้มาถึงโหนดนี้ (ในที่นี้คือการเดินทาง)
        self.path_cost = path_cost  # ราคารวมของเส้นทางจากจุดเริ่มต้นถึงโหนดนี้ (g)

    # ฟังก์ชันสำหรับการเปรียบเทียบใน Priority Queue (ใช้เมื่อ heap ต้องเรียงลำดับโหนด)
    def __lt__(self, other):
        return self.path_cost < other.path_cost


# คลาสสำหรับจำลองปัญหา (Problem) และโครงสร้างแผนที่
class RomaniaProblem:
    def __init__(self, initial, goal, graph):
        self.initial = initial  # จุดเริ่มต้น (เมืองเริ่มต้น)
        self.goal = goal        # จุดหมายปลายทาง (เมืองปลายทาง)
        self.graph = graph      # แผนที่เมืองและระยะทาง รูปแบบ Adjacency List {เมือง: {เมืองเชื่อม: ระยะทาง}}

    # ตรวจสอบว่าสถานะปัจจุบันเป็นเป้าหมายหรือยัง
    def is_goal(self, state):
        return state == self.goal

    # คืนค่ารายการเมืองที่สามารถเดินทางไปได้จากเมืองปัจจุบัน (Successors)
    def actions(self, state):
        return self.graph.get(state, {}).keys()

    # คืนค่าสถานะใหม่หลังจากดำเนินการ action (ในที่นี้ action คือเมืองปลายทาง)
    def result(self, state, action):
        return action

    # คืนค่าระยะทาง (cost) ระหว่างเมือง s ถึง s_prime
    def action_cost(self, s, action, s_prime):
        return self.graph[s][s_prime]


# ฟังก์ชัน Expand: กระจายโหนดลูกจากโหนดปัจจุบัน
# yield โหนดลูกทั้งหมดที่เดินทางไปได้จากโหนดนี้
def expand(problem, node):
    s = node.state  # ดึงสถานะปัจจุบัน (ชื่อเมือง)
    for action in problem.actions(s):  # วนทุกเมืองที่เชื่อมกับเมืองปัจจุบัน
        s_prime = problem.result(s, action)  # เมืองปลายทาง
        cost = node.path_cost + problem.action_cost(s, action, s_prime)  # g(n) = g(parent) + cost(edge)
        yield Node(state=s_prime, parent=node, action=action, path_cost=cost)


# อัลกอริทึม Best-First Search
# problem: วัตถุ RomaniaProblem ที่กำหนดจุดเริ่มต้น เป้าหมาย และแผนที่
# f: ฟังก์ชัน heuristic สำหรับจัดลำดับโหนด (เช่น f(n)=path_cost สำหรับ UCS)
# verbose: แสดงขั้นตอนการทำงานในแต่ละรอบ
def best_first_search(problem, f, verbose=False):
    # --- การเริ่มต้น (Initialization) ---
    node = Node(state=problem.initial)  # สร้างโหนดเริ่มต้น path_cost=0
    frontier = []  # Frontier = Priority Queue เก็บโหนดที่รอตรวจสอบ
    heapq.heappush(frontier, (f(node), node))  # เพิ่มโหนดเริ่มต้น (ค่า f, โหนด)
    reached = {problem.initial: node}  # Reached = โหนดที่ดีที่สุดที่เคยไปถึงแต่ละเมือง

    step = 0
    if verbose:  # แสดงหัวข้อขั้นตอน (ถ้าเปิดโหมด verbose)
        print("=" * 60)
        print("ขั้นตอนการทำงาน Best-First Search")
        print(f"จุดเริ่มต้น: {problem.initial} | เป้าหมาย: {problem.goal}")
        print("=" * 60)

    while frontier:  # ทำซ้ำจนกว่า Frontier จะว่าง หรือพบเป้าหมาย
        _, node = heapq.heappop(frontier)  # ดึงโหนดที่มีค่า f(n) น้อยที่สุด (Best-First)
        step += 1

        if verbose:
            print(f"\n--- รอบที่ {step} ---")
            print(f"ดึงโหนด: {node.state} (path_cost = {node.path_cost})")

        if problem.is_goal(node.state):  # Goal Test: ตรวจสอบว่าเป็นเป้าหมายหรือไม่
            if verbose:
                print(f">>> ถึงเป้าหมาย! {node.state}")
            return node # คืนค่าโหนดเป้าหมายกลับไป

        if verbose:
            children_added = []

        # Expand: กระจายโหนดลูกและเพิ่มเข้า Frontier
        for child in expand(problem, node):
            s = child.state
            # เพิ่มโหนดลูกเมื่อ: ยังไม่เคยไปถึง s หรือพบเส้นทางที่สั้นกว่าเดิม
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                heapq.heappush(frontier, (f(child), child))
                if verbose:
                    children_added.append(f"{s}({child.path_cost})")

        if verbose:
            if children_added:
                print(f"กระจายโหนดลูก: {', '.join(children_added)}")
            else:
                print("กระจายโหนดลูก: (ไม่มีโหนดใหม่ที่สั้นกว่า)")
            frontier_list = sorted([(fv, n.state) for fv, n in frontier])
            print(f"Frontier: {[(fv, s) for fv, s in frontier_list]}")

    return "failure"  # ไม่พบเส้นทาง (Frontier ว่างแต่ยังไม่ถึงเป้าหมาย)


# ==================== ข้อมูลแผนที่ ====================

# แผนที่ถนนโรมาเนีย: {เมือง: {เมืองที่เชื่อม: ระยะทาง(ไมล์)}}
romania_map = {
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Rimnicu Vilcea': 80, 'Fagaras': 99},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# ==================== ส่วนการรันโปรแกรม ====================

# สร้างปัญหา: หาเส้นทางจาก Oradea ไป Eforie
problem = RomaniaProblem('Drobeta', 'Eforie', romania_map)

# เรียก Best-First Search โดยใช้ f(n) = path_cost (เทียบเท่า Uniform Cost Search)
# verbose=True แสดงขั้นตอนการทำงานในแต่ละรอบ
result_node = best_first_search(problem, lambda n: n.path_cost, verbose=True)

# สร้างเส้นทางจากผลลัพธ์ (Path Reconstruction)
print("\n" + "=" * 60)
print("สรุปผลลัพธ์")
print("=" * 60)
if result_node != "failure":
    path = []
    current = result_node
    # ย้อนกลับจากโหนดเป้าหมายไปหาจุดเริ่มต้นผ่าน parent
    while current:
        path.append(current.state)
        current = current.parent
    path.reverse()  # เรียงจากจุดเริ่มต้นไปเป้าหมาย
    print(f"เส้นทางที่พบ: {' -> '.join(path)}")
    print(f"ระยะทางรวม: {result_node.path_cost} ไมล์")
else:
    print("ไม่พบเส้นทาง")