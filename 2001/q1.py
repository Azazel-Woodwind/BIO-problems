def q1a():
    friends = [x for x in range(1, int(input("Number of friends: ")) + 1)]
    words = int(input("Number of words in rhyme: "))

    pointer = 0
    while (len(friends) > 1):
        pointer += words - 1
        pointer %= len(friends)
        friends.pop(pointer)

    print("Friend", friends[0], "is left")

def clockwise(num_of_friends, words):
    friends = [x for x in range(1, num_of_friends + 1)]
    pointer = 0

    while (len(friends) > 1):
        pointer += words - 1
        pointer %= len(friends)
        friends.pop(pointer)

    return friends[0]

def anticlockwise(num_of_friends, words):
    friends = [x for x in range(1, num_of_friends + 1)]
    pointer = 0
    
    while (len(friends) > 1):
        pointer = pointer - words + 1
        pointer %= len(friends)
        friends.pop(pointer)
        pointer -= 1

    return friends[0]

def q1c():
    words = 1
    while (1):
        if clockwise(100, words) == anticlockwise(100, words):
            break
        words += 1

    print(words)
    

def main():
    q1c()

if __name__ == "__main__":
    main()