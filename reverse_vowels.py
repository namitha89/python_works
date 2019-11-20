# Write a function that takes a string as input and reverse only the vowels of a string.
vowels = 'aeiou'

def get_reversed_vowel(input_string):
    for letter in input_string[::-1]:
        if letter in vowels:
            yield(letter)

def reverseVowels(input_string):
    reversed_vowel = get_reversed_vowel(input_string)
    new_word = ''
    for letter in input_string:
        if letter in vowels:
            new_word += reversed_vowel.next()
        else:
            new_word += letter
    return new_word

input_string = "leetcodeo"
print(reverseVowels(input_string))
