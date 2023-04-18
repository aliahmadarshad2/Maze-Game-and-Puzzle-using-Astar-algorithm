maze = [[0, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 1]]
    
# The start and end points are represented as tuples
start = (5, 0)
end = (0, 5)

# The heuristic function is the Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# The A* search function
def astar(maze, start, end):
    # The open and closed sets
    openset = set()
    closedset = set()
    # Current point is the starting point
    current = start
    # Add the starting point to the open set
    openset.add(current)
    # While the open set is not empty
    while openset:
        # Find the item in the open set with the lowest G + H score
        current = None
        current_f_score = None
        for pos in openset:
            pos_f_score = g_score.get(pos, 0) + heuristic(pos, end)
            if current is None or pos_f_score < current_f_score:
                current_f_score = pos_f_score
                current = pos
        # If it is the item we want, retrace the path and return it
        if current == end:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path
        # Remove the item from the open set
        openset.remove(current)
        # Add it to the closed set
        closedset.add(current)
        # Loop through the node's children/siblings
        for node in get_neighbors(maze, current):
            # If it is already in the closed set, skip it
            if node in closedset:
                continue
            # Otherwise if it is already in the open set
            if node in openset:
                # Check if we beat the G score
                new_g_score = g_score.get(current, 0) + heuristic(current, node)
                if node not in g_score or new_g_score < g_score[node]:
                    # If so, update the node to have a new parent
                    came_from[node] = current
                    # And a new G score
                    g_score[node] = new_g_score
            else:
                # If it isn't in the open set, calculate the G and H score for the node
                g_score[node] = g_score.get(current, 0) + heuristic(current, node)
                h_score[node] = heuristic(node, end)
                # Set the parent to our current item
                came_from[node] = current
                # Add it to the set
                openset.add(node)
    # Throw an exception if there is no path
    raise ValueError('No Path Found')

# Returns a list of available neighbors for a node
def get_neighbors(maze, node):
    neighbors = []
    # Check the node above the current node
    if node[0] > 0 and maze[node[0] - 1][node[1]] != 0:
        neighbors.append((node[0] - 1, node[1]))
    # Check the node to the right of the current node
    if node[1] < len(maze[node[0]]) - 1 and maze[node[0]][node[1] + 1] != 0:
        neighbors.append((node[0], node[1] + 1))
    # Check the node below the current node
    if node[0] < len(maze) - 1 and maze[node[0] + 1][node[1]] != 0:
        neighbors.append((node[0] + 1, node[1]))
    # Check the node to the left of the current node
    if node[1] > 0 and maze[node[0]][node[1] - 1] != 0:
        neighbors.append((node[0], node[1] - 1))
    return neighbors

# The cost from start along best known path.
g_score = {start: 0}
# Estimated total cost from start to goal through y.
h_score = {start: heuristic(start, end)}
# The came from map
came_from = {}
# Run the search algorithm
path = astar(maze, start, end)

# Print the path
print(path)

# Print the maze with the path
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if (y, x) in path:
            print('x', end='')
        elif maze[y][x] == 0:
            print('#', end='')
        else:
            print('#', end='')
    print()