###############################################################

# To create a skeleton function, use the pass keyword within it.
def skeletonFunction():
    pass

###############################################################

# This a basic function that will print back to the terminal:
def howdyFunction():
    print("Howdy! I am a function.")

# This will execute the function set up above:
howdyFunction()

###############################################################

# This is a basic function which allows a single parameter:
def mathsFunction(inputvar):
    if inputvar.isnumeric():
        print("The calculation result is: ", int(inputvar) * 2)
    else:
        print("A number was not inputted")

user_input_maths = input("Please input a number: ")
mathsFunction(user_input_maths)

###############################################################

# This is a function with a return:
def returnFunction(inputvar):
    if inputvar.isnumeric():
        result = int(inputvar) * 2
    else:
        print("A number was not inputted")
    return result

user_input_return = input("Please input a number: ")
returnFunction_result = returnFunction(user_input_return)
print(returnFunction_result)

###############################################################