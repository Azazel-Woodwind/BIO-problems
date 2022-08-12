def simplify(numerator, denom):
    while numerator % 2 == 0 and denom % 2 == 0:
        numerator /= 2
        denom /= 2

    while numerator % 5 == 0 and denom % 5 == 0:
        numerator /= 5
        denom /= 5

    return numerator, denom

def get_unsimplified_fraction(decimal):
    denom = 1
    while (decimal != int(decimal)):
        decimal = round(decimal * 10, 4)
        denom *= 10

    return decimal, denom

def get_score(decimal):
    score = 1
    numerator, denom = get_unsimplified_fraction(decimal)
    numerator, denom = simplify(numerator, denom)
    
    while (numerator > 0):
        score *= numerator % 10
        numerator = int(numerator / 10)

    while (denom > 0):
        score *= denom % 10
        denom = int(denom / 10)

    return score


def q1a():
    decimal = float(input())

    numerator, denom = get_unsimplified_fraction(decimal)

    numerator, denom = simplify(numerator, denom)

    print(int(numerator), "/", int(denom))

def q1b():
    decimal = 0.0001
    denominators = set()
    while decimal < 0.9999:
        _, denom = get_unsimplified_fraction(decimal)
        _, denom = simplify(_, denom)
        denominators.add(denom)
        decimal += 0.0001

    print(len(denominators))

def q1c():
    decimal = 0.0001
    scores = dict()
    while decimal < 1:
        score = get_score(decimal)
        scores[score] = decimal
        decimal = round(decimal + 0.0001, 4)

    print(scores[max(scores.keys())])

def main():
    q1b()

if __name__ == "__main__":
    main()