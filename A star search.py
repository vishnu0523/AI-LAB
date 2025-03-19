import heapq

def a_star(graph, start, goal, heuristic, detailed_output=False):
    """
    A* search algorithm to find the shortest path in a graph, with detailed output including a tree-like structure.

    Args:
        graph (dict): A dictionary representing the graph.
        start: The starting node.
        goal: The goal node.
        heuristic (function): A heuristic function that estimates the cost from a node to the goal.
        detailed_output (bool): If True, prints detailed information about the algorithm's progress.

    Returns:
        tuple: A tuple containing:
            - list: A list of nodes representing the shortest path from start to goal, or None if no path exists.
            - dict: A dictionary containing the g_scores of each node at the end of the search.
            - dict: A dictionary containing the f_scores of each node at the end of the search.
            - dict: A dictionary representing the search tree (node: parent).
    """

    open_set = [(0, start)]
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    came_from = {}  # Used to reconstruct the path and build the search tree
    search_tree = {} # dictionary representing the search tree (node: parent)
    search_tree[start] = None  # Root of the tree has no parent


    if detailed_output:
        print(f"Starting A* search from {start} to {goal}")
        print(f"Initial g_score[{start}] = {g_score[start]}")
        print(f"Initial f_score[{start}] = {f_score[start]}")
        print(f"Open set: {open_set}")

    iteration = 0
    while open_set:
        iteration += 1
        if detailed_output:
            print(f"\n--- Iteration {iteration} ---")

        f_score_current, current = heapq.heappop(open_set)

        if detailed_output:
            print(f"  Expanding node: {current} (f_score = {f_score_current})")

        if current == goal:
            if detailed_output:
                print(f"  Goal node {goal} reached!")
            path = reconstruct_path(came_from, current)
            return path, g_score, f_score, search_tree

        if detailed_output:
            print(f"  Neighbors of {current}: {graph[current]}")

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost

            if detailed_output:
                print(f"    Checking neighbor: {neighbor}, cost = {cost}, tentative_g_score = {tentative_g_score}")

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                if detailed_output:
                    if neighbor not in g_score:
                        print(f"      New node found: {neighbor}")
                    else:
                        print(f"      Better path to {neighbor} found (g_score: {g_score[neighbor]} -> {tentative_g_score})")

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                search_tree[neighbor] = current  # Add to the search tree

                if detailed_output:
                    print(f"      g_score[{neighbor}] = {g_score[neighbor]}")
                    print(f"      f_score[{neighbor}] = {f_score[neighbor]}")

                if (f_score[neighbor], neighbor) not in open_set:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    if detailed_output:
                        print(f"      Adding {neighbor} to open set with f_score = {f_score[neighbor]}")
                        print(f"      Open set: {open_set}")
                else:
                    if detailed_output:
                        print(f"      {neighbor} already in open set. Not adding again.")
            else:
                if detailed_output:
                    print(f"    Not a better path to {neighbor}. Skipping.")

    if detailed_output:
        print(f"No path found from {start} to {goal}")
    return None, g_score, f_score, search_tree


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path


def print_tree(tree, root, indent=""):
    """Prints the search tree in a tree-like structure."""
    print(indent + root)
    for node, parent in tree.items():
        if parent == root and node != root:  # Avoid printing the root as its own child
            print_tree(tree, node, indent + "  ")

# Example Usage:
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'D': 1, 'E': 4},
    'C': {'A': 2, 'F': 8},
    'D': {'B': 1, 'G': 3},
    'E': {'B': 4, 'H': 6},
    'F': {'C': 8, 'I': 7},
    'G': {'D': 3},
    'H': {'E': 6},
    'I': {'F': 7}
}

def heuristic(node, goal):
    return 0

start_node = 'A'
goal_node = 'I'

path, g_scores, f_scores, search_tree = a_star(graph, start_node, goal_node, heuristic, detailed_output=True)

if path:
    print(f"\nShortest path from {start_node} to {goal_node}: {path}")
    print(f"Final g_scores: {g_scores}")
    print(f"Final f_scores: {f_scores}")
    print("\nSearch Tree:")
    print_tree(search_tree, start_node)  # Print the search tree

else:
    print(f"No path found from {start_node} to {goal_node}")
