def get_multipliers(num):
    sorted_num = sorted(str(num))
    answers = [str(i) for i in range(2, 10) if (sorted(str(num * i))) == sorted_num]

    return answers

def is_anagram(num):
    sorted_num = sorted(str(num))
    for i in range(2, 10):
        if (sorted(str(num * i))) == sorted_num:
            return True
    return False

def q1c():
    count = 0
    for i in range(100000, 1000000):
        if is_anagram(i):
            if len(set(str(i))) == len(str(i)):
                count += 1

    print(count)

def q1b():
    answers = list()
    for i in range(2, 10):
        num = 85247910 / i
        if (num == int(num)):
            num = int(num)
            if (sorted(str(num))) == (sorted(str(85247910))):
                answers.append(num)

    print(answers)

def q1a():
    while (1):
        answers = get_multipliers(int(input()))

        if len(answers) == 0:
            print("NO")
        else:
            print(" ".join(answers))

def main():
    q1a()

if __name__ == "__main__":
    main()