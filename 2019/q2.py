MOVEMENTS = {"U" : 1, "R" : 1, "D" : -1, "L" : -1}
DIRECTIONS = list(MOVEMENTS)

def turn_right():
    global current_direction

    pointer = (DIRECTIONS.index(current_direction) + 1) % len(DIRECTIONS)
    current_direction = DIRECTIONS[pointer]

def turn_left():
    global current_direction

    pointer = (DIRECTIONS.index(current_direction) - 1) % len(DIRECTIONS)
    current_direction = DIRECTIONS[pointer]

def move_forward(x, y):
    global current_direction

    if (current_direction == "U" or current_direction == "D"):
        y += MOVEMENTS[current_direction]
    else:
        x += MOVEMENTS[current_direction]

    return x, y

def try_to_move_forward(trail_coords, x, y):
    next_x, next_y = move_forward(x, y)
    if (next_x, next_y) in trail_coords:
        count = 0
        while (next_x, next_y) in trail_coords and count < 4:
            turn_right()
            next_x, next_y = move_forward(x, y)
            count += 1
        if count == 4:
            return None
        trail_coords[(x, y)] = 0
        return (next_x, next_y)
    else:
        trail_coords[(x, y)] = 0
        return (next_x, next_y)

def q2a():
    global current_direction
    current_direction = DIRECTIONS[0]

    inp = input("Input: ")
    data = inp.split()
    trail_age, instr, moves = int(data[0]), data[1], int(data[2])
    #FL
    x, y = 0, 0
    trail_coords = {}
    nextMove = 0
    move = 0
    
    while move < moves:
        dir = instr[nextMove]
        if dir == "F":
            data = try_to_move_forward(trail_coords, x, y)
            if data == None:
                return x, y
            x, y = data[0], data[1]
        elif dir == "R":
            turn_right()
            data = try_to_move_forward(trail_coords, x, y)
            if data == None:
                return x, y
            x, y = data[0], data[1]
        elif dir == "L":
            turn_left()
            data = try_to_move_forward(trail_coords, x, y)
            if data == None:
                return x, y
            x, y = data[0], data[1]

        move += 1
        nextMove += 1
        nextMove %= len(instr)

        for trail_coord, age in list(trail_coords.items()):
            trail_coords[trail_coord] += 1
            age += 1
            if age == trail_age:
                del trail_coords[trail_coord]

    return x, y

#2c = 21 * 21 - 1 = 440

def main():
    while (1):
        print(q2a())


if __name__ == "__main__":
    main()