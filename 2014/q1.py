def get_bounds(num):
    odds = [2 * n + 1 for n in range(num)]
    lower = 1
    for i in range(1, len(odds)):
        if odds[i] == 0:
            continue
        lucky_num = odds[i]
        if lucky_num > num:
            print(odds)
            return lower, lucky_num
        elif lucky_num < num:
            lower = lucky_num
        count = 0
        for x in range(len(odds)):
            if odds[x] != 0:
                count += 1
            if (count % lucky_num == 0):
                odds[x] = 0
            


def q1a():
    while (1):
        num = int(input())
        print(get_bounds(num))
        

def main():
    q1a()

if __name__ == "__main__":
    main()