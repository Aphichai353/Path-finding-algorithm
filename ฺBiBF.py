import heapq

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
# Helper Class
# ----------------------------
class NodeInfo:
    def __init__(self, parent=None, g=0):
        self.parent = parent
        self.g = g


# ----------------------------
# Reconstruct Path
# ----------------------------
def reconstruct(meet, reached_f, reached_b):
    path_f = []
    cur = meet
    while cur is not None:
        path_f.append(cur)
        cur = reached_f[cur].parent
    path_f.reverse()

    path_b = []
    cur = reached_b[meet].parent
    while cur is not None:
        path_b.append(cur)
        cur = reached_b[cur].parent

    return path_f + path_b


# ----------------------------
# Bidirectional Best-First (UCS style)
# ----------------------------
def bidirectional_search(graph, start, goal):

    frontier_f = [(0, start)]
    frontier_b = [(0, goal)]

    reached_f = {start: NodeInfo(None, 0)}
    reached_b = {goal: NodeInfo(None, 0)}

    best_cost = float("inf")
    meet_node = None

    while frontier_f and frontier_b:

        # Termination condition
        if frontier_f[0][0] + frontier_b[0][0] >= best_cost:
            break

        # Expand smaller top
        if frontier_f[0][0] <= frontier_b[0][0]:
            g, node = heapq.heappop(frontier_f)

            if g != reached_f[node].g:
                continue

            for nbr, dist in graph.get(node, {}).items():
                newg = g + dist

                if nbr not in reached_f or newg < reached_f[nbr].g:
                    reached_f[nbr] = NodeInfo(node, newg)
                    heapq.heappush(frontier_f, (newg, nbr))

                    # Check meeting
                    if nbr in reached_b:
                        total = newg + reached_b[nbr].g
                        if total < best_cost:
                            best_cost = total
                            meet_node = nbr
        else:
            g, node = heapq.heappop(frontier_b)

            if g != reached_b[node].g:
                continue

            for nbr, dist in graph.get(node, {}).items():
                newg = g + dist

                if nbr not in reached_b or newg < reached_b[nbr].g:
                    reached_b[nbr] = NodeInfo(node, newg)
                    heapq.heappush(frontier_b, (newg, nbr))

                    if nbr in reached_f:
                        total = newg + reached_f[nbr].g
                        if total < best_cost:
                            best_cost = total
                            meet_node = nbr

    if meet_node is None:
        return None, None

    path = reconstruct(meet_node, reached_f, reached_b)
    return path, best_cost


# ----------------------------
# Run
# ----------------------------
start = "Saraburi"
goal = "ChiangMai"

path, cost = bidirectional_search(TH_ROADS, start, goal)

print("Path:", " -> ".join(path))
print("Total distance:", cost, "km")