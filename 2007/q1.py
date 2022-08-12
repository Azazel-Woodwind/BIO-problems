def get_number_count(numbers):
    counts = dict()
    for x in numbers:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    return counts

def q1c():
    numbers = [x for x in range(1, 11)]
    combinations = []

    for i in range(len(numbers)):
        for x in range(len(numbers)):
            for y in range(len(numbers)):
                for z in range(len(numbers)):
                    for p in range(len(numbers)):
                        a = sorted([numbers[i], numbers[x], numbers[y], numbers[z], numbers[p]])
                        if sum(a) == 15 and len(set(a)) >= 2 and a not in combinations:
                            combinations.append(a)

    print(len(combinations))

def q1a():
    score = 0
    numbers = [int(input()) for _ in range(5)]
    total = sum(numbers)

    number_count = get_number_count(numbers)

    for number in number_count:
        count = number_count[number]
        if count > 1:
            score += (count * (count - 1)) / 2

    for i in range(len(numbers) - 1):
        if total - numbers[i] == 15:
            score += 1
        for x in range(i + 1, len(numbers)):
            pair_tot = numbers[i] + numbers[x]
            if pair_tot == 15:
                score += 1
            if total - pair_tot == 15:
                score += 1

    if total - numbers[-1] == 15:
        score += 1

    print(int(score))

def main():
    q1c()

if __name__ == "__main__":
    main()
