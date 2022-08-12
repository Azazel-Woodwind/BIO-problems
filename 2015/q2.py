from typing import List, Tuple

def is_on_grid(x, y):
    return 0 <= x <= 9 and 0 <= y <= 9

def get_all_surrounding_coords(x, y):
    return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]

def get_surrounding_existing_coords(x, y):
    return [(x, y) for x, y in get_all_surrounding_coords(x, y) if is_on_grid(x, y)]

def valid_coordinate(x, y, grid):
    if not is_on_grid(x, y) or grid[y][x]:
        return False

    for x, y in get_surrounding_existing_coords(x, y):
        if grid[y][x]:
            return False

    return True

def is_placeable(ship_length : int, grid : List[bool], x : int, y : int, is_horizontal : bool) -> List[Tuple[int]]:
    coords = []

    if is_horizontal:
        for i in range(ship_length):
            if not valid_coordinate(x + i, y, grid):
                return None
            coords.append(((x + i), y))
    else:
        for i in range(ship_length):
            if not valid_coordinate(x, y - i, grid):
                return None
            coords.append((x, y - i))

    return coords

def game(a, c, m):
    r = 0
    grid = [[False for _ in range(10)] for _ in range(10)]
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    for nShip in ships:
        placed = False
        while not placed:     
            r = (a * r + c) % m
            temp = r
            x = temp % 10
            temp = int(r / 10)
            original_y = temp % 10
            y = 9 - original_y

            #print(x, original_y)

            r = (a * r + c) % m
            isEven = (r % 2) == 0
            letter = "H" if isEven else "V"

            ship_coords = is_placeable(nShip, grid, x, y, isEven)
            if (ship_coords is not None):
                print(x, original_y, letter)
                placed = True
                for x, y in ship_coords:
                    grid[y][x] = True

    return grid

def q2a():
    a, c, m = list(map(int, input("Input: ").split()))
    grid = game(a, c, m)

    for row in grid:
        print(list(map(int, row)))
                    
def main():
    q2a()

if __name__ == "__main__":
    main()