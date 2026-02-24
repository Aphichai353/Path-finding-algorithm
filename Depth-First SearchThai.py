import heapq # นำเข้าไลบรารีสำหรับจัดการ Priority Queue (คิวลำดับความสำคัญ)

# 1. ข้อมูลพิกัด (ใช้สำหรับแสดงผล หรือคำนวณ Heuristic ในอนาคต)
TH_COORDS = {
    "Bangkok": (13.7563, 100.5018), "Ayutthaya": (14.3532, 100.5680),
    "Chonburi": (13.3611, 100.9847), "Pattaya": (12.9236, 100.8825),
    "Kanchanaburi": (14.0228, 99.5328), "HuaHin": (12.5684, 99.9577),
    "Rayong": (12.6814, 101.2816), "NakhonPathom": (13.8199, 100.0622),
    "Saraburi": (14.5289, 100.9101), "NakhonRatchasima": (14.9799, 102.0977),
    "KhonKaen": (16.4419, 102.8350), "UdonThani": (17.4138, 102.7870),
    "Phitsanulok": (16.8211, 100.2659), "ChiangMai": (18.7883, 98.9853),
}

# 2. ข้อมูลเส้นทางและระยะทาง (Adjacency List)
TH_ROADS = {
    "Bangkok": {"Ayutthaya": 80, "NakhonPathom": 60, "Chonburi": 85, "Kanchanaburi": 130, "HuaHin": 200, "Saraburi": 110},
    "Ayutthaya": {"Bangkok": 80, "Saraburi": 75, "Phitsanulok": 330},
    "NakhonPathom": {"Bangkok": 60, "Kanchanaburi": 95},
    "Kanchanaburi": {"NakhonPathom": 95, "Bangkok": 130},
    "Chonburi": {"Bangkok": 85, "Pattaya": 50, "Rayong": 80},
    "Pattaya": {"Chonburi": 50, "Rayong": 65},
    "Rayong": {"Pattaya": 65, "Chonburi": 80},
    "HuaHin": {"Bangkok": 200},
    "Saraburi": {"Bangkok": 110, "Ayutthaya": 75, "NakhonRatchasima": 170},
    "NakhonRatchasima": {"Saraburi": 170, "KhonKaen": 200},
    "KhonKaen": {"NakhonRatchasima": 200, "UdonThani": 110},
    "UdonThani": {"KhonKaen": 110},
    "Phitsanulok": {"Ayutthaya": 330, "ChiangMai": 370},
    "ChiangMai": {"Phitsanulok": 370},
}

# คลาส Node ตามนิยามในอัลกอริทึม
class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state          # เก็บชื่อจังหวัดปัจจุบัน
        self.parent = parent        # เก็บโหนดก่อนหน้า
        self.path_cost = path_cost  # ระยะทางสะสม

# ฟังก์ชัน Expand สำหรับกระจายโหนดลูก
def expand(graph, node):
    s = node.state                  # ดึงชื่อจังหวัดปัจจุบัน
    for next_state, weight in graph.get(s, {}).items(): # วนลูปหาจังหวัดที่ติดกันและระยะทาง
        cost = node.path_cost + weight # คำนวณราคารวมใหม่ g(n') = g(n) + c(n, a, n')
        yield Node(state=next_state, parent=node, path_cost=cost) # ส่งคืนโหนดลูกใหม่

# อัลกอริทึม Depth-First Search (DFS)
def depth_first_search(initial, goal, graph):
    node = Node(state=initial)      # สร้างโหนดเริ่มต้น
    if node.state == goal:          # ถ้าเริ่มที่เป้าหมายเลย
        return node
    frontier = [node]               # ใช้ List เป็น Stack สำหรับ DFS
    reached = {initial}             # เก็บรายชื่อจังหวัดที่เคยไปแล้ว

    while frontier:                 # ทำงานตราบเท่าที่ยังมีจังหวัดใน Stack
        node = frontier.pop()       # ดึงจังหวัดล่าสุดออกมาสำรวจ (ดิ่งลงลึก)
        if node.state == goal:      # ถ้าจังหวัดนี้คือเป้าหมาย
            return node
        for child in expand(graph, node): # ขยายโหนดไปยังจังหวัดข้างเคียง
            s = child.state         # ดึงชื่อจังหวัดลูก
            if s not in reached:   # ถ้ายังไม่เคยไปจังหวัดนี้มาก่อน
                reached.add(s)      # บันทึกว่าสำรวจจังหวัดนี้แล้ว
                frontier.append(child) # ใส่ลงใน Stack เพื่อรอสำรวจ
    return None                     # คืนค่าว่างหากหาเส้นทางไม่เจอ

# --- ส่วนทดสอบการทำงาน ---
START = "Bangkok"                   # กำหนดจุดเริ่มต้น
GOAL = "UdonThani"                  # กำหนดจุดหมาย

# เรียกใช้การค้นหาแบบ Depth-First Search
result_node = depth_first_search(START, GOAL, TH_ROADS)

# แสดงผลเส้นทาง
if result_node:                     # ถ้าพบโหนดเป้าหมาย
    path = []                       # สร้างรายการเก็บชื่อเมือง
    curr = result_node              # เริ่มจากโหนดปลายทาง
    while curr:                     # วนลูปย้อนกลับไปถึงจุดเริ่มต้น
        path.append(curr.state)     # เพิ่มชื่อเมืองลงใน path
        curr = curr.parent          # ย้อนไปที่ parent
    print(f"เส้นทางจาก {START} ไป {GOAL}: {' -> '.join(reversed(path))}") # พิมพ์เส้นทาง
    print(f"ระยะทางรวมทั้งหมด: {result_node.path_cost} กม.") # พิมพ์ระยะทางรวม
    
    # เพิ่มการแสดงรายละเอียดจังหวัดที่ผ่านและระยะทางแต่ละช่วง
    print(f"\nจังหวัดที่ผ่านทั้งหมด ({len(path)} จังหวัด):")
    for i, province in enumerate(reversed(path), 1):
        print(f"  {i}. {province}")
    
    # คำนวณและแสดงระยะทางแต่ละช่วง
    print(f"\nรายละเอียดเส้นทางพร้อมระยะทาง:")
    reversed_path = list(reversed(path))
    cumulative_distance = 0
    for i in range(len(reversed_path) - 1):
        current_province = reversed_path[i]
        next_province = reversed_path[i+1]
        distance = TH_ROADS.get(current_province, {}).get(next_province, 0)
        cumulative_distance += distance
        print(f"  {current_province} -> {next_province}: {distance} กม. (รวมสะสม: {cumulative_distance} กม.)")
    
    print(f"จำนวนจังหวัดที่ผ่าน: {len(path) - 1} จังหวัด (ไม่รวมจุดเริ่มต้น)")
else:                               # ถ้าหาไม่เจอ
    print("ไม่พบเส้นทาง")