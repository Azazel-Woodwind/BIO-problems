import math

def get_primes_up_to(num):
    primes = [2]
    for i in range(3, num - 1, 2):
        index = 0
        isPrime = True
        while (primes[index] <= math.sqrt(i)):
            if i % primes[index] == 0:
                isPrime = False
                break
            index += 1

        if isPrime:
            primes.append(i)

    return primes

def get_num_of_prime_pairs_inefficient(num):
    primes = get_primes_up_to(num)
    prime_pairs = set()

    for prime in primes:
        if (num - prime) in primes:
            pair = (prime, num - prime)
            prime_pairs.add(tuple(sorted(pair)))

    return len(prime_pairs)

def get_num_of_prime_pairs_efficient(num):
    primes = get_primes_up_to(num)
    length = len(primes)
    count = 0
    index = 0

    while index < length and primes[index] <= num // 2:
        if num - primes[index] in primes:
            count += 1
        index += 1

    return count

def get_prime_pairs(num):
    primes = get_primes_up_to(num)
    length = len(primes)
    pairs = set()
    index = 0

    while index < length and primes[index] <= num // 2:
        if num - primes[index] in primes:
            pair = (primes[index], num - primes[index])
            pairs.add(pair)
        index += 1

    return pairs

def q1c():
    count = 0
    for i in range(5, 50):
        if get_num_of_prime_pairs_efficient(i) == 0:
            count += 1

    print(count)

def q1b():
    print(get_prime_pairs(46))

def q1a():
    while (1):
        print(get_num_of_prime_pairs_efficient(int(input())))

def main():
    q1b()

if __name__ == "__main__":
    main()