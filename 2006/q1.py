def get_alphabet_count(word):
    alphabet = dict()

    for i in range(65, 91):
        alphabet[chr(i)] = 0

    for letter in word.upper():
        alphabet[letter] += 1

    return alphabet

def q1a():
    word1 = input()
    word2 = input()

    alph_count_1 = get_alphabet_count(word1)
    alph_count_2 = get_alphabet_count(word2)

    if alph_count_1 == alph_count_2:
        print("Anagrams")
    else:
        print("Not Anagrams")

def main():
    q1a()

if __name__ == "__main__":
    main()

#1b = 6
#1c = 21

