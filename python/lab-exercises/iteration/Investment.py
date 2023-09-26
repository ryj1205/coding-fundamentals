""" Investment Application """

initial_investment = 100
interest_rate = 0.10
target_value = 1000
number_of_years = 0

while initial_investment < target_value:
    initial_investment *= (1 + interest_rate)
    number_of_years += 1

print("It would take", number_of_years, "years to grow your initial investment to £", target_value)
