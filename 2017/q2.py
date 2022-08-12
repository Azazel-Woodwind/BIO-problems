class Square():

    def __init__(self, top_left_dot, top_right_dot, bot_right_dot, bot_left_dot) -> None:
        self.top_left_dot = top_left_dot
        self.top_right_dot = top_right_dot
        self.bot_left_dot = bot_left_dot
        self.bot_right_dot = bot_right_dot
        self.owner = None

    def setOwner(self, owner) -> None:
        self.owner = owner

    def getOwner(self) -> int:
        return self.owner

    def isComplete(self) -> bool:
        return self.top_left_dot.linked_with(self.top_right_dot) and self.top_right_dot.linked_with(self.bot_right_dot) and \
            self.bot_right_dot.linked_with(self.bot_left_dot) and self.bot_left_dot.linked_with(self.top_left_dot)

    def __str__(self) -> str:
        if self.owner == 1:
            return "X"
        elif self.owner == 2:
            return "O"
        return "*"

    def print_dots(self):
        print(self.top_left_dot.pos, self.top_right_dot.pos, self.bot_right_dot.pos, self.bot_left_dot.pos)


class Player():

    def __init__(self, pos, modifier, player_number) -> None:
        self.pos = pos
        self.modifier = modifier
        self.player_number = player_number
        self.count = 0

    def getNextPos(self, grid) -> int:
        self.pos += self.modifier
        while self.pos > len(grid):
            self.pos -= len(grid)

        while not grid[self.pos - 1].is_linkable():
            self.pos += 1
            if self.pos > 36:
                self.pos -= 36

        #print(self.pos)
        return self.pos


class Dot():

    def __init__(self, pos) -> None:
        self.pos = pos
        self.upper_dot = {}
        self.adjacent_dots = {}

    def get_adjacent_dots(self, grid):
        if self.pos > 6:
            self.upper_dot[grid[self.pos - 1 - 6]] = False
        if self.pos % 6:
            self.adjacent_dots[grid[self.pos - 1 + 1]] = False
        if self.pos <= 30:
            self.adjacent_dots[grid[self.pos - 1 + 6]] = False
        if (self.pos - 1) % 6:
            self.adjacent_dots[grid[self.pos - 1 - 1]] = False

    def is_linkable(self) -> bool:
        return False in self.upper_dot.values() or False in self.adjacent_dots.values()

    def linked_with(self, dot) -> bool:
        return (dot in self.upper_dot and self.upper_dot[dot] == True) or (dot in self.adjacent_dots and self.adjacent_dots[dot] == True)

    def link_first_dot(self, player_number) -> None:
        for dot in self.upper_dot:
            if not self.upper_dot[dot]:
                self.upper_dot[dot] = True
                dot.link_dot(self)
                return
        temp_dict = self.adjacent_dots.copy() if player_number == 1 else reversed(self.adjacent_dots)

        for dot in temp_dict:
            if not self.adjacent_dots[dot]:
                self.adjacent_dots[dot] = True
                dot.link_dot(self)
                return

    def link_dot(self, dot) -> None:
        if dot in self.upper_dot:
            self.upper_dot[dot] = True
            return
        self.adjacent_dots[dot] = True

    def print_state(self):
        print("Position:", self.pos)
        print("Adjacent dots: ")
        for i in self.upper_dot:
            print(i.pos, self.upper_dot[i])
        for i in self.adjacent_dots:
            print(i.pos, self.adjacent_dots[i])



def q2a() -> None:
    inp = input("Input: ")
    p1_pos, p1_mod, p2_pos, p2_mod, moves = map(int, inp.split())
    grid = [Dot(pos) for pos in range(1, 37)]
    squares = [Square(grid[x], grid[x + 1], grid[x + 7], grid[x + 6]) for x in range(len(grid)) if x <= 28 and (x + 1) % 6]    
    for dot in grid:
        dot.get_adjacent_dots(grid)
    p1 = Player(p1_pos, p1_mod, 1)
    p2 = Player(p2_pos, p2_mod, 2)
    players = [p1, p2]
    player_pointer = 0

    for turn in range(moves):
        square_gained = False
        current_player = players[player_pointer]
        next_pos = current_player.getNextPos(grid)
        dot = grid[next_pos - 1]
        dot.link_first_dot(current_player.player_number)

        for square in squares:
            if square.isComplete() and square.owner is None:
                square_gained = True
                square.setOwner(current_player.player_number)
                current_player.count += 1

        if not square_gained:
            player_pointer = (player_pointer + 1) % len(players)

    for i in range(0, len(squares), 5):
        print(squares[i], squares[i + 1], squares[i + 2], squares[i + 3], squares[i + 4])

    print(p1.count, p2.count)

def main() -> None:
    while (1):
        q2a()

if __name__ == "__main__":
    main()
