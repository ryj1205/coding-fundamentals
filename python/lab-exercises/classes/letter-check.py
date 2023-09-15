###########################################################################################################
# Goal:
# Write a class called 'Lettercheck'
    # Create an attribute called vowels and fill it with vowels
    # Create a method that takes a single letter and checks if it is a vowel
    # return true or false
# Rewrite the class so you can create different objects for finding if letters are members of different letter groups
# [http://rinkworks.com/words/lettergroups.shtml]
###########################################################################################################

class LetterCheck:

    def __init__(self,passedletter,passedgroup):
        self.group = passedgroup
        self.letter = passedletter

    def groupCheck(self):
        if (self.letter in self.group):
            return True
        else:
            return False

###########################################################################################################

group_vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
group_straightlines = {"A", "E", "F", "H", "I", "K", "L", "M", "T", "W", "X", "Y", "Z"}

###########################################################################################################

vowel_test = LetterCheck("a", group_vowels)
print(vowel_test.groupCheck())

non_vowel_test = LetterCheck("b", group_vowels)
print(non_vowel_test.groupCheck())

straight_lines_test = LetterCheck("b", group_straightlines)
print(straight_lines_test.groupCheck())

###########################################################################################################
