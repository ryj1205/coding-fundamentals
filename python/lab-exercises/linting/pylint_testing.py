""" Testing the usage of PyLint """

def count(sequence, item):

    """ Count function """

    sequence_num = 0
    for current_num in sequence:
        if current_num == item:
            sequence_num += 1
    return sequence_num
