""" Age Range Sorter """

ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,
        78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,
        11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

# 1. Record the length of the ages List in a variable (you'll need it later) Display the length.
ages_length = len(ages)
print("OG List Length - ", ages_length)
print("############################################")

# 2. Display these ages one on each line: Tip: Use a for loop to read each number.
for age in ages:
    print(age)

print("############################################")

# 3. Add one year to every age!
for age in ages:
    age += 1
    print(age)

print("############################################")

# 4. Our code only takes into account those people in the age range of 16-65 (inclusively)
# Please delete all ages which are outside this range.

i = 0
ages_range = ages
ages_range_length = len(ages_range)

while i < ages_range_length:
    if ages_range[i] < 16 or ages_range[i] > 65:
        del(ages_range[i])
        ages_range_length = len(ages_range)
        i = 0
    else:
        print(ages_range[i])
        i += 1

print("############################################")
print("Ages between 16 and 65 - ", ages_range_length)
print("############################################")

# 5. Display the count of 16-25 year olds.
ages_count_16to25 = 0
for age in ages_range:
    if age >= 16 and age <= 25:
        ages_count_16to25 += 1
print("Ages between 16 to 25 - ", ages_count_16to25)

# 6. Invoke the sort method on the ages List.
ages.sort()
