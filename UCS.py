import heapq

# ----------------------------
# Graph Data
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
# Uniform Cost Search
# ----------------------------
def uniform_cost_search(graph, start, goal):
    # priority queue: (cost, state, path)
    frontier = [(0, start, [])]
    visited_cost = {}

    while frontier:
        cost, state, path = heapq.heappop(frontier)

        # Skip if we already found a cheaper path
        if state in visited_cost and visited_cost[state] <= cost:
            continue

        visited_cost[state] = cost
        path = path + [state]

        # Goal test when popping (as in UCS)
        if state == goal:
            return path, cost

        # Expand neighbors
        for neighbor, distance in graph.get(state, {}).items():
            new_cost = cost + distance
            heapq.heappush(frontier, (new_cost, neighbor, path))

    return None, float("inf")


# ----------------------------
# Run UCS
# ----------------------------
start = "NakhonPathom"
goal = "Ayutthaya"

path, total_cost = uniform_cost_search(TH_ROADS, start, goal)

if path:
    print("Path:", " -> ".join(path))
    print("Total distance:", total_cost, "km")
else:
    print("No path found")