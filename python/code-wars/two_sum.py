""" Two Sum """

# Write a function that takes an array of numbers (integers for the tests) and a target number. It
# should find two different items in the array that, when added together, give the target value.
# The indices of these items should then be returned in a tuple / list (depending on your language)
# like so: (index1, index2).
# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be
# accepted. The input will always be valid (numbers will be an array of length 2 or greater, and
# all of the items will be numbers; target will always be the sum of two different items from that array).

###################################################################################################

def two_sum(numbers, target):

    num_check = False

    if (numbers[0] + numbers[1] == target):
        num_check = True

    

    print(num_check)

###################################################################################################

two_sum([1, 2, 2], 4)

###################################################################################################

# sample_test_cases = [
#     numbers           target   valid results
#     ([1 ,2, 3],            4,  ((0,2), (2,0))),
#     ([1234,5678,9012], 14690,  ((1,2), (2,1))),
#     ([2, 2, 3],            4,  ((0,1), (1,0))),
# ]

# def sample_tests():
#     for numbers, target, valid_results in sample_test_cases:
#         def _():
#             actual = two_sum(numbers, target)
#             msg = []
#             if isinstance(actual, list): msg.append('The result should be a tuple, not a list')
#             msg.append(f'{actual} should be either {valid_results[0]} or {valid_results[1]}')
#             test.expect(actual in valid_results, '\n'.join(msg))
