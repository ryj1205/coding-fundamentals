""" Test the count program from applications """

import pytest
from applications import count

def test_count_zeros():
    """ Test the count function with zeros """
    assert count.count([0, 0, 0], 0) == 3


def test_count_string():
    """ Test the count function with string """
    assert count.count(["a", "a", "a"], "a") == 3


def test_count_minus():
    """ Test the count function with minus integers """
    assert count.count([-1, -3, -5, -4], -1) == 1


def test_count_normalnum():
    """ Test the count function with integers """
    assert count.count([1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1], 1) == 2
