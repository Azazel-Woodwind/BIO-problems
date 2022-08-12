import time


def get_char_to_pos():
    char_to_pos = dict()
    for i in range(65, 91):
        char_to_pos[chr(i)] = i - 64

    return char_to_pos

CHAR_TO_POS = get_char_to_pos()
POS_TO_CHAR = dict()
for char in CHAR_TO_POS:
    POS_TO_CHAR[CHAR_TO_POS[char]] = char


def letter_fibonacci(letter1, letter2, n):
    if n < 3:
        return (CHAR_TO_POS[letter1], CHAR_TO_POS[letter2])[n - 1]

    a = CHAR_TO_POS[letter1]
    b = CHAR_TO_POS[letter2]

    for _ in range(n - 2):
        c = a + b
        c = c - 26 if c > 26 else c
        a = b
        b = c

    return b

def q1c():
    count = 2
    # while(1):
    #     count += 1
    #     letter = letter_fibonacci("C", "C", count)
    #     if letter == 3 and letter_fibonacci("C", "C", count + 1) == 3:
    #         print(count + 1, flush=True)
    #         time.sleep(0.5)

    # while(1):
    #     count += 1
    #     letter = letter_fibonacci("C", "C", count)
    #     print(POS_TO_CHAR[letter], count, flush=True)
    #     time.sleep(0.2)

    
    print((1000000000000000000 - 2) % 84)
    print(POS_TO_CHAR[letter_fibonacci("C", "C", 64)])

def q1a():
    inp = input()
    args = inp.split(" ")
    print(POS_TO_CHAR[letter_fibonacci(args[0], args[1], int(args[2]))])

def main():
    q1c()

if __name__ == "__main__":
    main()

#C C A C C A C C