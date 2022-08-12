from typing import List, Tuple

VALID_OUTPUT = [[1, 0, 1, 0, 0], [1, 0, 1, 0, 0], [1, 0, 0, 0, 0], [1, 0, 1, 0, 0], [1, 0, 0, 0, 0]]

def convert_pos_to_coords(current_pos : int) -> List[int]:
    pos = current_pos - 1
    row = pos // 5
    col = pos % 5
    return row, col

def get_adjacent_coords(row : int, col : int) -> List[List[int]]:
    return [[row, col + 1], [row, col - 1], [row + 1, col], [row - 1, col]]

def migrate(row : int, col : int, grid : List[int], rofset : int, cofset : int) -> Tuple[int]:
    grid[row][col] -= 4
    adjacent_coords = get_adjacent_coords(row, col)
    coord_col_ofset = 0

    for coord in adjacent_coords:
        coord[1] += coord_col_ofset
        grid_width = len(grid[0])
        grid_height = len(grid)

        if coord[0] >= grid_height:
            grid.append([0 for _ in range(grid_width)])
        elif coord[0] < 0:
            grid.insert(0, [0 for _ in range(grid_width)])
            coord[0] = 0
            rofset += 1
        elif coord[1] >= grid_width:
            for row in grid.copy():
                row.append(0)
        elif coord[1] < 0:
            for row in grid.copy():
                row.insert(0, 0)
            coord[1] = 0
            coord_col_ofset += 1
            cofset += 1

        grid[coord[0]][coord[1]] += 1

    return rofset, cofset

def game(current_pos : int, sequence : List[int], num_of_steps) -> None:
    grid = [[0 for _ in range(5)] for _ in range(5)]
    rofset = 0
    cofset = 0
    integer_pointer = 0

    for step in range(num_of_steps):
        row, col = convert_pos_to_coords(current_pos)
        row += rofset
        col += cofset

        grid[row][col] += 1

        overcrowded = True
        while (overcrowded):
            overcrowded = False
            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    if grid[row][col] >= 4:
                        overcrowded = True
                        rofset, cofset = migrate(row, col, grid, rofset, cofset)

        current_pos += sequence[integer_pointer]
        integer_pointer = (integer_pointer + 1) % len(sequence)

        while (current_pos > 25):
            current_pos -= 25

    return [grid[row][cofset : cofset + 5] for row in range(rofset, rofset + 5)]


def q2a() -> None:
    data = map(int, input("Input: ").split())
    current_pos, _, num_of_steps = data
    sequence = list(map(int, input("Sequence: ").split()))

    grid = game(current_pos, sequence, num_of_steps)

    for row in grid:
        print(" ".join(list(map(str, row))))

def q2c():
    count = 0
    for starting_pos in range(1, 26):
        for num1 in range(25):
            for num2 in range(25):
                for num3 in range(25):
                    if game(starting_pos, [num1, num2, num3], 8) == VALID_OUTPUT:
                        print()
                        print(starting_pos, 3, 8)
                        print(num1, num2, num3)
                        count += 1

    print(count)

def main():
    q2a()

if __name__ == "__main__":
    main()