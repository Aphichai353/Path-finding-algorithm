"""
โปรแกรม Depth-First Search (DFS) สำหรับหาเส้นทางระหว่างเมือง
โดยใช้แผนที่ประเทศโรมาเนีย (Romania Map) เป็นกราฟ
DFS สำรวจดิ่งลงลึกก่อน (ลึกก่อนกว้าง) โดยใช้ Stack (LIFO)
"""

import sys
import io

# แก้ไข encoding สำหรับ Windows ให้แสดงภาษาไทยได้
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


# ==================== คลาสและฟังก์ชันหลัก ====================

# คลาส Node: เก็บข้อมูลแต่ละโหนดในการค้นหา
class Node:
    """เก็บข้อมูลโหนด: สถานะ, โหนดพ่อแม่, การกระทำ, และระยะทางสะสม"""
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state          # สถานะปัจจุบัน (ชื่อเมือง)
        self.parent = parent        # โหนดพ่อแม่ (ใช้ย้อนรอยเส้นทาง Path Reconstruction)
        self.action = action        # การกระทำที่ทำให้มาถึงโหนดนี้
        self.path_cost = path_cost  # ระยะทางสะสมจากจุดเริ่มต้น (g)


# คลาส RomaniaProblem: จำลองปัญหาและโครงสร้างแผนที่
class RomaniaProblem:
    def __init__(self, initial, goal, graph):
        self.initial = initial      # จุดเริ่มต้น (เมืองเริ่มต้น)
        self.goal = goal            # จุดหมายปลายทาง
        self.graph = graph          # แผนที่รูปแบบ Adjacency List {เมือง: {เมืองเชื่อม: ระยะทาง}}

    def is_goal(self, state):
        """ตรวจสอบว่าสถานะปัจจุบันเป็นเป้าหมายหรือไม่"""
        return state == self.goal

    def actions(self, state):
        """คืนค่ารายการเมืองที่เดินทางไปได้จากเมืองปัจจุบัน"""
        return self.graph.get(state, {}).keys()

    def result(self, state, action):
        """คืนค่าสถานะใหม่หลังดำเนินการ (action = เมืองปลายทาง)"""
        return action

    def action_cost(self, s, action, s_prime):
        """คืนค่าระยะทางระหว่างเมือง s ถึง s_prime"""
        return self.graph[s][s_prime]


# ฟังก์ชัน Expand: กระจายโหนดลูกจากโหนดปัจจุบัน
def expand(problem, node):
    """yield โหนดลูกทั้งหมดที่เดินทางไปได้จากโหนดนี้"""
    s = node.state
    for action in problem.actions(s):
        s_prime = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s_prime)
        yield Node(state=s_prime, parent=node, action=action, path_cost=cost)


# อัลกอริทึม Depth-First Search (DFS)
# ใช้ Stack (LIFO) - โหนดที่ใส่ทีหลังจะถูกดึงออกมาก่อน (ดิ่งลงลึกก่อนกว้าง)
# verbose: แสดงขั้นตอนการทำงานในแต่ละรอบ
def depth_first_search(problem, verbose=False):
    # --- การเริ่มต้น (Initialization) ---
    node = Node(state=problem.initial)
    if problem.is_goal(node.state):  # กรณีพิเศษ: จุดเริ่มต้นเป็นเป้าหมาย
        return node

    frontier = [node]  # Stack: ใช้ list + pop() (ดึงจากท้าย) = LIFO
    reached = {problem.initial}  # เก็บเมืองที่เคยไป เพื่อป้องกัน Cycle (วนซ้ำ)

    step = 0
    if verbose:
        print("=" * 60)
        print("ขั้นตอนการทำงาน Depth-First Search")
        print(f"จุดเริ่มต้น: {problem.initial} | เป้าหมาย: {problem.goal}")
        print("=" * 60)

    while frontier:
        node = frontier.pop()  # ดึงโหนดล่าสุดที่ใส่เข้ามา (Stack = ลึกก่อนกว้าง)
        step += 1

        if verbose:
            print(f"\n--- รอบที่ {step} ---")
            print(f"ดึงโหนด: {node.state} (path_cost = {node.path_cost})")

        if problem.is_goal(node.state):  # Goal Test
            if verbose:
                print(f">>> ถึงเป้าหมาย! {node.state}")
            return node

        if verbose:
            children_added = []

        for child in expand(problem, node):
            s = child.state
            if s not in reached:  # เฉพาะเมืองที่ยังไม่เคยไป
                reached.add(s)
                frontier.append(child)  # ใส่ที่ท้าย Stack
                if verbose:
                    children_added.append(f"{s}({child.path_cost})")

        if verbose:
            if children_added:
                print(f"กระจายโหนดลูก: {', '.join(children_added)}")
            else:
                print("กระจายโหนดลูก: (ไม่มีโหนดใหม่)")
            # แสดง Stack จากบนลงล่าง (ตัวบนจะถูก pop ออกก่อน)
            stack_display = [(n.state, n.path_cost) for n in reversed(frontier)]
            print(f"Frontier (Stack): {stack_display}")

    return "failure"

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
problem = RomaniaProblem('Drobeta', 'Neamt', romania_map)

# เรียก DFS โดยใส่ verbose=True เพื่อแสดงขั้นตอนการทำงาน
result = depth_first_search(problem, verbose=True)

# สร้างเส้นทางจากผลลัพธ์ (Path Reconstruction)
print("\n" + "=" * 60)
print("สรุปผลลัพธ์")
print("=" * 60)
if result != "failure":
    path = []
    current = result
    # ย้อนกลับจากโหนดเป้าหมายไปหาจุดเริ่มต้นผ่าน parent
    while current:
        path.append(current.state)
        current = current.parent
    path.reverse()
    print(f"เส้นทางที่พบ (DFS): {' -> '.join(path)}")
    print(f"ระยะทางรวม: {result.path_cost} ไมล์")
else:
    print("ไม่พบเส้นทาง")