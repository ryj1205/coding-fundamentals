
# A selection in it's most basic form:

#   if <test>:
#       perform an action
#   else:
#       perform an alternative action

number_required = 10
inputvar = int(input("Please input a number: "))

if inputvar == number_required:
    print("Congratulations! You typed the correct number (" + str(number_required) + ") into the prompt!")
else:
    print("Apologies - you inputted the incorrect number.")

if inputvar < 10:
    print("You have inputted a single digit number")
elif inputvar < 100:
    print("You have inputted a two digit number")
elif inputvar < 1000:
    print("You have inputted a three digit number")

print("You have reached the end of the program - thanks for playing!")