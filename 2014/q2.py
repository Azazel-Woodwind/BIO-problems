from __future__ import annotations

RED_LINES = {1 : ((-1, 0), (1, 0)), 2 : ((0, -1), (0, 1)), 3 : ((0, -1), (-1, 0)), 4 : ((-1, 0), (0, 1)), 5 : ((1, 0), (0, 1)), 6 : ((0, -1), (1, 0))}
GREEN_LINES = {1 : ((0, -1), (0, 1)), 2 : ((-1, 0), (1, 0)), 3 : ((1, 0), (0, 1)), 4 : ((0, -1), (1, 0)), 5 : ((0, -1), (-1, 0)), 6 : ((-1, 0), (0, 1))}


class Square():

    def __init__(self, row : int, column : int, type : int, grid_size : int) -> None:
        self.row = row
        self.column = column
        self.visited_red = False
        self.visited_green = False
        self.type = type
        self.red_connected_coords = [(row + offset[0], column + offset[1]) for offset in RED_LINES[type] 
                                    if Square.is_valid_coord(row + offset[0], column + offset[1], grid_size)]
        self.green_connected_coords = [(row + offset[0], column + offset[1]) for offset in GREEN_LINES[type]
                                    if Square.is_valid_coord(row + offset[0], column + offset[1], grid_size)]
        
    def __repr__(self) -> str:
        return f"""Row: {self.row} Column: {self.column} Type: {self.type}
                Red connected coords: {self.red_connected_coords}
                Green connected coords: {self.green_connected_coords}"""
        
    @staticmethod
    def is_valid_coord(row, col, grid_size):
        return 0 <= row < grid_size and 0 <= col < grid_size
    

def find_loop(square : Square, grid : list[Square], isRed : bool, count : int) -> bool:   
    if isRed:
        square.visited_red = True
    else:
        square.visited_green = True
    
    connected_count = 0
    connected_square_coords : list[tuple[int]] = square.red_connected_coords if isRed else square.green_connected_coords
    for row, col in connected_square_coords:
        connected_square : Square = grid[row][col]
        visited = connected_square.visited_red if isRed else connected_square.visited_green
        connected_square_neighbours = connected_square.red_connected_coords if isRed else connected_square.green_connected_coords
        connected = (square.row, square.column) in connected_square_neighbours
        if not visited:
            if connected:
                count += 1
                return find_loop(connected_square, grid, isRed, count)
            else:
                return False, count
        elif connected:
            connected_count += 1
            
    if connected_count == 2:
        return True, count
    return False, count

def game(grid):
    red_score = 0
    green_score = 0
    
    for row in grid:
        for square in row:
            if not square.visited_red:
                loop_found, count = find_loop(square, grid, True, 1)
                if loop_found:
                    red_score += count
            if not square.visited_green:
                loop_found, count = find_loop(square, grid, False, 1)
                if loop_found:
                    green_score += count
            
    return red_score, green_score

def q2c():
    grid = []

def q2a():
    grid_size = int(input())
    grid = []
    
    for row in range(grid_size):
        row_contents = list(map(int, input().split()))
        grid.append([Square(row, col, square_type, grid_size) for col, square_type in enumerate(row_contents)])

    red, green = game(grid)
    print(red, green)
    
                
def main():
    q2a()

if __name__ == "__main__":
    main()