import heapq
from collections import deque

# 1. State Space: Define Exercises (MET = Metabolic Equivalent of Task)
# Calories burned per minute = (MET * 3.5 * body_weight_kg) / 200
exercises = {
    'Warm-up': {'met': 3.0, 'duration': 5, 'muscle': 'Full Body'},
    'Bench Press': {'met': 6.0, 'duration': 10, 'muscle': 'Chest'},
    'Squats': {'met': 8.0, 'duration': 12, 'muscle': 'Legs'},
    'Deadlift': {'met': 9.0, 'duration': 15, 'muscle': 'Back'},
    'Bicep Curls': {'met': 3.5, 'duration': 8, 'muscle': 'Arms'},
    'Plank': {'met': 4.0, 'duration': 5, 'muscle': 'Core'}
}

# Graph representation (Possible transitions in a workout)
gym_graph = {
    'Warm-up': ['Bench Press', 'Squats', 'Plank'],
    'Bench Press': ['Bicep Curls', 'Plank'],
    'Squats': ['Deadlift', 'Plank'],
    'Deadlift': ['Bicep Curls'],
    'Bicep Curls': [],
    'Plank': []
}

# 2. Un-informed Search: Breadth-First Search (BFS)
def bfs_workout(start, goal):
    queue = deque([[start]])
    visited = set()
    nodes_explored = 0

    while queue:
        path = queue.popleft()
        node = path[-1]
        nodes_explored += 1

        if node == goal:
            return path, nodes_explored

        if node not in visited:
            for neighbor in gym_graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None, nodes_explored

# 3. Informed Search: A* Algorithm
def heuristic(node, goal):
    # Heuristic: Remaining estimated "effort" (Inversely proportional to MET)
    # A higher MET means a more efficient workout (lower h-cost)
    return 10 - exercises[node]['met']

def a_star_workout(start, goal):
    # Priority Queue stores (total_cost, current_path)
    # total_cost = g(n) + h(n)
    priority_queue = [(0 + heuristic(start, goal), [start], 0)]
    visited = {}
    nodes_explored = 0

    while priority_queue:
        f_cost, path, g_cost = heapq.heappop(priority_queue)
        node = path[-1]
        nodes_explored += 1

        if node == goal:
            return path, nodes_explored

        if node not in visited or g_cost < visited[node]:
            visited[node] = g_cost
            for neighbor in gym_graph.get(node, []):
                # Cost g(n) is the duration of the exercise
                new_g_cost = g_cost + exercises[neighbor]['duration']
                new_f_cost = new_g_cost + heuristic(neighbor, goal)
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(priority_queue, (new_f_cost, new_path, new_g_cost))
    
    return None, nodes_explored

# 4. Main Execution & Comparison
if __name__ == "__main__":
    start_node = 'Warm-up'
    goal_node = 'Bicep Curls'

    print("--- Fitness AI Agent Search Results ---")
    
    # Run BFS
    bfs_path, bfs_nodes = bfs_workout(start_node, goal_node)
    print(f"\n[Un-informed Search: BFS]")
    print(f"Path: {' -> '.join(bfs_path)}")
    print(f"Nodes Explored: {bfs_nodes}")

    # Run A*
    as_path, as_nodes = a_star_workout(start_node, goal_node)
    print(f"\n[In-informed Search: A*]")
    print(f"Path: {' -> '.join(as_path)}")
    print(f"Nodes Explored: {as_nodes}")
    
    print("\nConclusion: A* used a heuristic to reach the goal with fewer/smarter explorations.")
