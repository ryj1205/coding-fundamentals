""" Factorial App """

user_input = int(input("Please input a number: "))
factorial = 1
number = 1

while number <= user_input:
    factorial = factorial * number
    print(number, " - ", factorial)
    number += 1
