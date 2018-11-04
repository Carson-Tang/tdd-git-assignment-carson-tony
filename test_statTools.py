import pytest
from statTools import *

list_data = [0, 9, 6, 2, 4, 7, 20, 1, 5, 4, 8]
list_data2 = [0, 9, 6, 2, 4, 7, 20, 1, 5, 4, 8, 18]
empty_data = []
# Value frequencies - value:frequency
def test_mode_1():
    assert(mode(empty_data) == None)
# 0:1, 1:1, 2:1, 4:2, 5:1, 6:1, 7:1, 8:1, 9:1, 20:1
def test_mode_2():
    assert(mode(list_data) == 4)
# 0:1, 1:1, 2:2, 4:2, 5:1, 6:1, 7:1, 8:1, 9:1, 18:1, 20:1
def test_mode_3():
    assert(mode(list_data2) == [2, 4])

# sum = 66, elements = 11, mean = 6, ans = 296/11
def test_variance_1():
    assert(variance(list_data) == 296/11)
# sum = 84, elements = 12, mean = 7, ans = 428/12 = 107/3
def test_variance_2():
    assert(variance(list_data2) == 107/3)

