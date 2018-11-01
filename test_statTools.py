import pytest
from statTools import *

list_data = [0, 9, 6, 2, 4, 7, 10, 1, 5, 4, 8]
empty_data = []
# Value frequencies - value:frequency
def test_mode_1():
    assert(mode(empty_data) == 0)
# 0:1, 1:1, 2:1, 4:2, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1
def test_mode_2():
    assert(mode(list_data) == 4)
list_data.append(2)
# 0:1, 1:1, 2:2, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1
def test_mode_3():
    assert(mode(list_data) == 2)


