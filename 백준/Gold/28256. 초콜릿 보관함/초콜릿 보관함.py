def bfs(grid, start, visited):
    queue = [start]
    visited[start[0]][start[1]] = True
    count = 0
    while queue:
        current = queue.pop(0)
        count += 1
        for neighbor in get_neighbors(grid, current):
            if not visited[neighbor[0]][neighbor[1]]:
                visited[neighbor[0]][neighbor[1]] = True
                queue.append(neighbor)
    return count


def get_neighbors(grid, cell):
    neighbors = []
    if cell[0] > 0 and grid[cell[0] - 1][cell[1]] == "O":
        neighbors.append((cell[0] - 1, cell[1]))
    if cell[0] < len(grid) - 1 and grid[cell[0] + 1][cell[1]] == "O":
        neighbors.append((cell[0] + 1, cell[1]))
    if cell[1] > 0 and grid[cell[0]][cell[1] - 1] == "O":
        neighbors.append((cell[0], cell[1] - 1))
    if cell[1] < len(grid[0]) - 1 and grid[cell[0]][cell[1] + 1] == "O":
        neighbors.append((cell[0], cell[1] + 1))
    return neighbors


def find_connected_components(grid):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    counts = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O" and not visited[i][j]:
                counts.append(bfs(grid, (i, j), visited))
    return counts


T = int(input())

for _ in range(T):
    grid = []
    for _ in range(3):
        row = list(input())
        grid.append(row)

    # print(grid)
    nums = list(map(int, input().split()))
    lst = find_connected_components(grid)
    # print(lst)
    if nums[0] == len(lst):
        if nums[1:] == sorted(lst):
            print(1)
        else:
            print(0)
    else:
        print(0)