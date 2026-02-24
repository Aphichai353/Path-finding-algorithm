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
def depth_limited_search(graph, start, goal, limit):
    
    # frontier = stack (LIFO)
    frontier = [(start, [start], 0)]  # (state, path, depth)
    result = "failure"
    
    while frontier:
        state, path, depth = frontier.pop()

        # Goal test
        if state == goal:
            return path
        
        # Depth check
        if depth > limit:
            result = "cutoff"
        
        else:
            # Expand if no cycle
            for neighbor in graph.get(state, {}):
                if neighbor not in path:  # avoid cycle
                    frontier.append((neighbor, path + [neighbor], depth + 1))
    
    return result


# ----------------------------
# Run DLS
# ----------------------------
start = "Pattaya"
goal = "UdonThani"
limit = 6

result = depth_limited_search(TH_ROADS, start, goal, limit)

print("Result:", result)