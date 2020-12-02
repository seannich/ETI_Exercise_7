import pytest
from mycalculator.my_calculator_functions import *

'''
@pytest.mark.parametrize("a,b,result",[(1,2,3), (2,4,6)])
def test_add(a,b,result):
    value = add(a,b)
    assert value == result


def test_add_negative_positive():
    value = add(-1,2,3)
    assert value == 4

def test_add_negative_negative():
    value = add(-1,-2)
    assert value == -5
'''

def test_over_ten_variables():#add comment
    value = add(1,2,3,4,5,6,7,8,9,10,11,12)
    assert value == "Error: >10 Values"

def test_multiplication():
    value = multiply(1,1,1,1,1,1,1,1,1,1)
    assert value == 1

def test_multiplication_over_ten():
    value = multiply(1,1,1,1,1,1,1,1,1,1,1)
    assert value == "Error: >10 Values"