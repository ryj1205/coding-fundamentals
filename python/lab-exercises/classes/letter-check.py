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

    def __init__(self,passedletter):
        self.vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        self.letter = passedletter

    def vowelCheck(self):
        if (self.letter in self.vowels):
            return True
        else:
            return False

###########################################################################################################

letter_test = LetterCheck("a")
print(letter_test.vowelCheck())

letter_test = LetterCheck("b")
print(letter_test.vowelCheck())
