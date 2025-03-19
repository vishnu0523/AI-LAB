from collections import deque

GOAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, 0))  # Use tuple instead of list
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_zero(state):
    """Finds the position of the empty tile (0)."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return -1, -1

def generate_new_states(state):
    """Generates all possible moves from the current state."""
    x, y = find_zero(state)
    new_states = []
    
    for dx, dy in MOVES:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [list(row) for row in state]  # Convert tuples to lists
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            new_states.append(tuple(tuple(row) for row in new_state))  # Convert back to tuples
    return new_states

def bfs(initial_state):
    """Performs BFS to find the shortest path to the goal state."""
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == GOAL_STATE:
            return path + [current_state]  # Include goal state in solution
        
        for new_state in generate_new_states(current_state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))
    
    return None  # No solution found

if __name__ == "__main__":
    initial_state = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 0, 8)
    )
    
    solution = bfs(initial_state)
    
    if solution:
        print("Solution found!")
        for step in solution:
            for row in step:
                print(row)
            print()
    else:
        print("No solution found.")
