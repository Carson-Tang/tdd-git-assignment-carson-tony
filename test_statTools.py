import pytest
from statTools import *

list_data = [0, 9, 6, 2, 4, 7, 20, 1, 5, 4, 8]
list_data2 = [2, 9, 6, 2, 4, 7, 20, 1, 3, 4, 8, 18]
empty_data = []

def test_mean_1():
    pass
def test_mean_2():
    pass
def test_mean_3():
    pass

def test_median_1():
    pass
def test_median_2():
    pass
def test_median_3():
    pass

# Value frequencies - value:frequency
def test_mode_1():
    assert(mode(empty_data) == None)
# 0:1, 1:1, 2:1, 4:2, 5:1, 6:1, 7:1, 8:1, 9:1, 20:1
def test_mode_2():
    assert(mode(list_data) == 4)
# 1:1, 2:2, 3:1, 4:2, 5:1, 6:1, 7:1, 8:1, 9:1, 18:1, 20:1
def test_mode_3():
    assert(mode(list_data2) == [2, 4])

def test_range_1():
    pass
def test_range_2():
    pass
def test_range_3():
    pass

def test_lowerquartile_1():
    pass
def test_lowerquartile_2():
    pass
def test_lowerquartile_3():
    pass

# sum = 66, elements = 11, mean = 6, ans = 296/11
def test_variance_1():
    assert(variance(list_data) == round(296/11,3))
# sum = 84, elements = 12, mean = 7, ans = 416/12 = 104/3
def test_variance_2():
    assert(variance(list_data2) == round(104/3,3))


