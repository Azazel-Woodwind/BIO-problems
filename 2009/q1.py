import time

DIGIT_STRINGS = ("ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
VALUES = {DIGIT_STRINGS[i] : i + 1 for i in range(len(DIGIT_STRINGS))}

def get_digit(word):
    for digit in DIGIT_STRINGS:
        length = len(digit)
        index = 0
        for letter in word:
            if letter == digit[index]:
                index += 1
            if index == length:
                return VALUES[digit]

    return "NO"

def q1a():
    while (1):
        print(get_digit(input()))

def main():
    q1a()

if __name__ == "__main__":
    main()

#q1b -> 10
#q1c -> 18 do by hand