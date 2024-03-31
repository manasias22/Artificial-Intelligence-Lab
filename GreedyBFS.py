import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    priority_queue = [(heuristic(start), start)]
    visited = set()
    print("Path from", start_node, "to", goal_node, ": ", end="")
    while priority_queue:
        h, current = heapq.heappop(priority_queue)

        if current == goal:
            print(f"{current}({h})", end="\n")
            return current

        print(f"{current}({h})", end="-> ")

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic(neighbor), neighbor))

    return None

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E','G'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B','G'],
    'F': ['C'],
    'G': ['C','B','E']
}

# A simple heuristic function
def heuristic(node):
    return ord('G') - ord(node)  # Distance from node to goal node 'G'

start_node = 'A'
goal_node = 'G'

path = greedy_best_first_search(graph, start_node, goal_node, heuristic)



"""
OUTPUT:

PS C:\Desktop\CC> python GreedyBFS.py
Path from A to G : A(6)-> C(4)-> G(0)

"""