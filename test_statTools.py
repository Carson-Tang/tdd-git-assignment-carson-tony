import pytest
from statTools import *

list_data = [0, 9, 6, 2, 4, 7, 20, 1, 5, 4, 8]
list_data2 = [2, 9, 6, 2, 4, 7, 20, 1, 3, 4, 8, 18]
list_data3 = [1, 2, 3]
empty_data = []


def test_mean_1():
    assert(mean(empty_data) == -1)
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
# empty list, ans = empty list
def test_mode_1():
    assert(mode(empty_data) == [])
# 0:1, 1:1, 2:1, 4:2, 5:1, 6:1, 7:1, 8:1, 9:1, 20:1
# 4 is most frequent
def test_mode_2():
    assert(mode(list_data) == [4])
# 1:1, 2:2, 3:1, 4:2, 5:1, 6:1, 7:1, 8:1, 9:1, 18:1, 20:1
# 2 and 4 are most frequent
def test_mode_3():
    assert(mode(list_data2) == [2, 4])


def test_range_1():
    pass
def test_range_2():
    pass
def test_range_3():
    pass


# sorted list = [0, 1, 2, 4, 4, 5, 6, 7, 8, 9, 20]
# split = [0, 1, 2, 4, 4] [6, 7, 8, 9, 20]
# split lower half = [0, 1] 2 [4, 4] , ans = 2
def test_lowerquartile_1():
    assert(lower_quartile(list_data) == 2)
# sorted list = [1, 2, 2, 3, 4, 4, 6, 7, 8, 9, 18, 20]
# split = [1, 2, 2, 3, 4, 4] [6, 7, 8, 9, 18, 20]
# split lower half = [1, 2] 2, 3 [4, 4], ans = (2+3)/2 = 2.5
def test_lowerquartile_2():
    assert(lower_quartile(list_data2) == 2.5)
# Empty list, ans = 0
def test_lowerquartile_3():
    assert(lower_quartile(empty_data) == None)


# sorted list = [0, 1, 2, 4, 4, 5, 6, 7, 8, 9, 20]
# split = [0, 1, 2, 4, 4] [6, 7, 8, 9, 20]
# split top half = [6, 7] 8 [9, 20], ans = 8
def test_upperquartile_1():
    assert(upper_quartile(list_data) == 8)
# sorted list = [1, 2, 2, 3, 4, 4, 6, 7, 8, 9, 18, 20]
# split = [1, 2, 2, 3, 4, 4] [6, 7, 8, 9, 18, 20]
# split lower half = [6, 7] 8, 9 [18, 20], ans = (8+9)/2 = 8.5
def test_upperquartile_2():
    assert(upper_quartile(list_data2) == 8.5)
# list of length 3, ans = 0
def test_upperquartile_3():
    assert(upper_quartile(list_data3) == 0)


# sum = 66, elements = 11, mean = 6, ans = 296/11
def test_variance_1():
    assert(variance(list_data) == round(296/11,3))
# sum = 84, elements = 12, mean = 7, ans = 416/12 = 104/3
def test_variance_2():
    assert(variance(list_data2) == round(104/3,3))
# sum = 0, elements = 0, ans = None
def test_variance_3():
    assert(variance(empty_data) == 0)


def test_standard_deviation_1():
    pass
def test_standard_deviation_2():
    pass
def test_standard_deviation_3():
    pass


