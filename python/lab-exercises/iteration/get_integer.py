""" Integer Range App """

min_value = 1
max_value = 100
ask_counter = 0

user_input = int(input("Please enter a number: "))

while (user_input < min_value or user_input > max_value) and ask_counter <= 2:
    print("Error - that number isn't within the range specified")
    user_input = int(input("Please input a number between 1 and 100: "))
    ask_counter = ask_counter + 1

if ask_counter <= 2:
    print(user_input)
else:
    print('Error - cannot exceed three attempts')
