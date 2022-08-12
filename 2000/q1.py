def checker(group, password):
    for element in range(len(password) - 2 * group + 1):
        first = [password[element + x] for x in range(group)]
        second = [password[element + group + y] for y in range(group)]
        if(first == second):
            return True

while (1):

    password = input()
    n = 0
    element = 0
    max_loop = len(password) // 2

    for a in range(max_loop):
        if(checker(a + 1, password) == True):
            print("Rejected")
            exit()

    print("Accepted")