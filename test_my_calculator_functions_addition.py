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

def test_add_ten_variables():#add comment
    value = add(1,2,3,4,5,6,7,8,9,10,11, 12)
    assert value == "Error: >10 Values"

def test_sub_ten_variables():#add comment
    value = subtract(1,2,3,4,5,6,7,8,9,10,11, 12)
    assert value == "Error: >10 Values"

def test_multiply_ten_variables():#add comment
    value = multiply(1,2,3,4,5,6,7,8,9,10,11, 12)
    assert value == "Error: >10 Values"

def test_divide_ten_variables():#add comment
    value = divide(1,2,3,4,5,6,7,8,9,10,11, 12)
    assert value == "Error: >10 Values"

def test_divide_one_zero():
    value = divide(2, 0)
    assert value == ZeroDivisionError

def test_addition3_():#add comment
    value = add(1, 1, 1)
    assert value == 3

def test_additionminus_():#add comment
    value = add(5, -1)
    assert value == 4

def test_minusaddition_():#add comment
    value = subtract(10, 2,)
    assert value == 8

def test_minus3_():#add comment
    value = subtract(10, 2, 1)
    assert value == 7