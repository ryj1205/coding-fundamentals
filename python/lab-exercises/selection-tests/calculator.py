first_number = int(input("Please input your first number: "))
second_number = int(input("Please input your second number: "))

print("") # line break
print("What calculation would you like to perform with these numbers? ")
print("1. Add +")
print("2. Subtract -")
print("3. Multiply *")
print("4. Divide /")
print("5. Square s")
print("") # line break

user_selection = int(input("Please input the number of the option you want to select: "))

if (user_selection == 1):
    result = first_number + second_number
elif (user_selection == 2):
    result = first_number - second_number
elif (user_selection == 3):
    result = first_number * second_number
elif (user_selection == 4):
    result = first_number / second_number
elif (user_selection == 5):
    result = first_number ** second_number

print(result)