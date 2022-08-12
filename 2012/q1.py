import math

def get_distinct_prime_product(num):
    product = 1
    ub = math.ceil(math.sqrt(num))

    if (num % 2 == 0):
        product *= 2
        while num % 2 == 0:
            num /= 2

    quotient = 3
    while (num > 1):
        if (num % quotient == 0):
            product *= quotient
            while num % quotient == 0:
                num /= quotient

        quotient += 2

    if product == 1:
        return num
    
    return product

def get_primes_up_to(num):
    primes = [2]
    for i in range(3, num // 2 + 1, 2):
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

def q1c():
    
    counter = {}
    for i in range(2, 1000001):
        prime_product = get_distinct_prime_product(i)
        if counter.get(prime_product) is None:
            counter[prime_product] = 1
        else:
            counter[prime_product] += 1

    occurences = 0
    largest = 0
    for x in counter:
        if counter[x] > occurences:
            largest = x
            occurences = counter[x]

    print(largest)


    

def q1a():
    while (1):
        print(get_distinct_prime_product(int(input())))
        

def main():
    q1c()

if __name__ == "__main__":
    main()