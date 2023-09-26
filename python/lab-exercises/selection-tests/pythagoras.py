""" Pythagoras' Calculator: """

print("Pythagoras' Calculator: ")
print("1. Find the length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")

user_selection = int(input("Please input the number of the option you want to select: "))

if user_selection == 1:
    side_b = int(input("Please input the length of side B: "))
    side_c = int(input("Please input the length of side C: "))
    result = side_b ** 2 + side_c ** 2
    print("You selected option 3 to calculate the length of side A, which is:", result)
elif user_selection == 2:
    side_a = int(input("Please input the length of side A: "))
    side_c = int(input("Please input the length of side C: "))
    result = side_a ** 2 + side_c ** 2
    print("You selected option 3 to calculate the length of side B, which is:", result)
elif user_selection == 3:
    side_a = int(input("Please input the length of side A: "))
    side_b = int(input("Please input the length of side B: "))
    result = side_a ** 2 + side_b ** 2
    print("You selected option 3 to calculate the length of side C, which is:", result)
