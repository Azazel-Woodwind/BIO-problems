from http.client import OK


def generate_second_dial(first_dial, n):
    first_dial_temp = first_dial[:]
    second_dial = []
    step = n - 1
    pointer = 0
    while len(first_dial_temp) > 0:
        pointer += step
        pointer %= len(first_dial_temp)
        second_dial.append(first_dial_temp.pop(pointer))
        
    return second_dial



def q2a():
    first_dial = [chr(x) for x in range(65, 91)]
    inp = input("Input: ")
    data = inp.split(" ")
    n = int(data[0])
    word = data[1]
    second_dial = generate_second_dial(first_dial, n)
    print("".join(second_dial[0 : 6]))

    answer = ""
    for letter in word:
        answer += second_dial[first_dial.index(letter)]
        second_dial.append(second_dial.pop(0))

    
    print(answer)

def q2c():
    def encrypt_letter(letter):
        return key[letter]

    biggest = 0
    first_dial = [chr(x) for x in range(65, 91)]
    count = 0
    key = {}
    x = 5
    second_dial = generate_second_dial(first_dial, x)

    for letter, encrypted_letter in zip(first_dial, second_dial):
        key[letter] = encrypted_letter

    word = "ABCD"
    word = "".join(list(map(encrypt_letter, word)))
    while word != "ABCD":
        count += 1
        word = "".join(list(map(encrypt_letter, word)))
    
    if count > biggest:
        biggest = count

        
    # print(biggest)
        
    first_dial = [chr(x) for x in range(65, 91)]
    dials = []
    n = 1
    while (1):
        dial = generate_second_dial(first_dial, n)
        if dial in dials:
            break
        dials.append(dial)
        n += 1
        print(n)

    print(n)

def main():
    q2c()

if __name__ == "__main__":
    main()