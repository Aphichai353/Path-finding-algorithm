# ----------------------------
# Graph
# ----------------------------
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

# ----------------------------
# Depth-Limited Search
# ----------------------------
def depth_limited_search(graph, state, goal, limit, path):
    
    if state == goal:
        return path
    
    if limit == 0:
        return "cutoff"
    
    cutoff_occurred = False
    
    for neighbor in graph.get(state, {}):
        if neighbor not in path:   # avoid cycle
            result = depth_limited_search(
                graph,
                neighbor,
                goal,
                limit - 1,
                path + [neighbor]
            )
            
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return result
    
    if cutoff_occurred:
        return "cutoff"
    else:
        return "failure"


# ----------------------------
# Iterative Deepening Search
# ----------------------------
def iterative_deepening_search(graph, start, goal):
    
    depth = 0
    
    while True:
        result = depth_limited_search(graph, start, goal, depth, [start])
        
        print(f"Depth = {depth} -> {result}")
        
        if result != "cutoff":
            return result
        
        depth += 1


# ----------------------------
# Run IDS
# ----------------------------
start = "Pattaya"
goal = "UdonThani"

final_path = iterative_deepening_search(TH_ROADS, start, goal)

print("\nFinal Path:", final_path)