import heapq

# Maze design (0 = Rasta, 1 = Wall) [cite: 28]
maze = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

# Manhattan Heuristic: Goal tak ka andaza lagana [cite: 30]
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_list = []
    # Priority queue mein (f_score, position) rakhein ge
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start, []))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        
        if current == goal:
            return path + [current]
        
        if current in visited:
            continue
        visited.add(current)
        
        # Charon taraf check karna (Up, Down, Left, Right)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0:
                new_g = g + 1
                new_f = new_g + heuristic((x, y), goal)
                heapq.heappush(open_list, (new_f, new_g, (x, y), path + [current]))
    
    return None # Agar rasta na mile [cite: 31]

# Program chalana
result = a_star(maze, start, goal)
print("Shortest Path:", result)

