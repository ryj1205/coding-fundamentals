number = 1

while number <= 100:
    number_squared = number ** 2
    if number_squared >= 2000:
        break;
    print(number, " - ", number_squared)
    number += 1