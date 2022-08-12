def isValid(code):
    count = 10
    sum = 0
    for s in code:
        sum += count * int(s)
        count -= 1
    if sum % 11 == 0:
        return True
    return False

def swap(a, b, c):
    return a[0: b] + a[c] + a[b + 1: c] + a[b] + a[c + 1: ]

def main():
    number = input()
    multiplier = 10
    sum = 0

    for digit in number:
        if digit != '?':
            if digit == 'X':
                num = 10
            else:
                num = int(digit)
            sum += multiplier * num
        else:
            ok = multiplier
        multiplier -= 1

    temp = sum
    while (1):        
        if temp % 11 == 0 and (temp - sum) % ok == 0:
            answer = (temp - sum) / ok
            break
        temp += 1

    answer = 'X' if answer == 10 else answer
    print(answer)

    # code = "3201014525"

    # for i in range(len(code)):
    #     for x in range(i + 1, len(code)):
    #         num = swap(code, i, x)
    #         if isValid(num):
    #             print(num)


if __name__ == "__main__":
    main()
