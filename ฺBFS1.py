from collections import deque

# 1. กำหนดข้อมูลกราฟที่โจทย์ให้มา
TH_ROADS = {
  "Bangkok": {
    "Ayutthaya": 80, "NakhonPathom": 60, "Chonburi": 85,
    "Kanchanaburi": 130, "HuaHin": 200, "Saraburi": 110
  },
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

# 2. ฟังก์ชัน BREADTH-FIRST-SEARCH
def breadth_first_search(graph, start, goal):
    # ใน Python เราจะเก็บ Node ในรูปแบบ Tuple: (state_ปัจจุบัน, path_เส้นทางที่ผ่านมา)
    # node <- NODE(problem.INITIAL)
    initial_node = (start, [start])
    
    # if problem.IS-GOAL(node.STATE) then return node
    if start == goal:
        return initial_node[1]

    # frontier <- a FIFO queue, with node as an element
    # ใช้ deque เพราะมีประสิทธิภาพสูงเวลาดึงข้อมูลจากด้านหน้า (popleft)
    frontier = deque([initial_node])
    
    # reached <- {problem.INITIAL}
    # ใช้ Set ในการเก็บเมืองที่เคยเจาะไปแล้ว (ป้องกันการเดินวนลูป)
    reached = {start}

    # while not IS-EMPTY(frontier) do
    while frontier:
        # node <- POP(frontier)
        current_state, path = frontier.popleft()

        # for each child in EXPAND(problem, node) do
        # ดึงเมืองที่เชื่อมต่อกัน (neighbor) จาก Dictionary
        for neighbor in graph.get(current_state, {}):
            # s <- child.STATE
            s = neighbor
            child_path = path + [s]
            
            # if problem.IS-GOAL(s) then return child
            if s == goal:
                return child_path
            
            # if s is not in reached then
            if s not in reached:
                # add s to reached
                reached.add(s)
                # add child to frontier
                frontier.append((s, child_path))
                
    # return failure
    return None

# --- ส่วนทดสอบการทำงาน ---
start_city = "Bangkok"
goal_city = "ChiangMai"
result = breadth_first_search(TH_ROADS, start_city, goal_city)

if result:
    print(f"🎯 เส้นทางที่สั้นที่สุด (จำนวนก้าวน้อยสุด) จาก {start_city} ไป {goal_city}:")
    print(" -> ".join(result))
    
    # คำนวณระยะทางรวมจากเส้นทางที่ได้
    total_cost = 0
    for i in range(len(result) - 1):
        city_a = result[i]
        city_b = result[i+1]
        total_cost += TH_ROADS[city_a][city_b]
        
    print(f"🛣️ ระยะทางรวม: {total_cost} กม.")
else:
    print("❌ ไม่พบเส้นทางเชื่อมต่อ")