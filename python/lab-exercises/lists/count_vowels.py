""" Count Vowels App """

user_input = input("Please enter a word: ")
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
vowel_count = 0

for character in user_input:
    if character in vowels:
        vowel_count += 1

print(vowel_count)
