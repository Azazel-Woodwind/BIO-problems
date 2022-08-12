from collections import deque

RED_LINES = {1 : ((-1, 0), (1, 0)), 2 : ((0, -1), (0, 1)), 3 : ((0, -1), (-1, 0)), 4 : ((-1, 0), (0, 1)), 5 : ((1, 0), (0, 1)), 6 : ((0, -1), (1, 0))}
GREEN_LINES = {1 : ((0, -1), (0, 1)), 2 : ((-1, 0), (1, 0)), 3 : ((1, 0), (0, 1)), 4 : ((0, -1), (1, 0)), 5 : ((0, -1), (-1, 0)), 6 : ((-1, 0), (0, 1))}

def get_connections(grid, coord, is_red):
    row, col = coord
    type = grid[row][col]
    offsets = RED_LINES[type] if is_red else GREEN_LINES[type]
    
    return [(row + roffset, col + coffset) for roffset, coffset in offsets if is_valid_coord(grid, row + roffset, col + coffset)]
    
def is_valid_coord(grid, row, col):
    length = len(grid)
    return (0 <= row < length) and (0 <= col < length) 

def get_neighbours(grid, coord, is_red):
    neighbours = set()
    connections = get_connections(grid, coord, is_red)
    for connection in connections:
        if coord in get_connections(grid, connection, is_red):
            neighbours.add(connection)
            
    return neighbours

def find_loop_count_dfs(grid, coord, is_red, visited):
    stack = deque([coord])
    count = 0
    
    while stack:
        current_coord = stack.pop()
        if current_coord not in visited:
            visited_count = 0
            count += 1
            visited.add(current_coord)
            for neighbour in get_neighbours(grid, current_coord, is_red):
                if neighbour not in visited:
                    stack.append(neighbour)
                else:
                    visited_count += 1
                    
            if visited_count == 2:
                return count
            
    return 0

def game(grid):
    red_visited = set()
    green_visited = set()
    red_score = 0
    green_score = 0
    
    length = len(grid)
    for row in range(length):
        for col in range(length):
            coord = (row, col)
            if coord not in red_visited:
                red_score += find_loop_count_dfs(grid, coord, True, red_visited)
            
            if coord not in green_visited:
                green_score += find_loop_count_dfs(grid, coord, False, green_visited)
                
    return red_score, green_score

def q2a():
    grid_size = int(input("Grid size: "))
    grid = [list(map(int, input().split())) for _ in range(grid_size)]
    
    red_score, green_score = game(grid)
    
    print(f"{red_score} {green_score}")

def main():
    while True:
        q2a()

if __name__ == "__main__":
    main()