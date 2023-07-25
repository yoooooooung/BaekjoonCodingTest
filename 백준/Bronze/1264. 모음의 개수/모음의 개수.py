vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while 1:
    sentence = input()
    number_of_vowels = 0
    if sentence == '#':
        break
    else:
        for vowel in vowels:
            number_of_vowels += sentence.count(vowel)

    print (number_of_vowels)