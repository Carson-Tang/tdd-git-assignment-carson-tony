import pytest
from statTools import *

list_data = [0, 9, 6, 2, 4, 7, 20, 1, 5, 4, 8]
list_data2 = [2, 9, 6, 2, 4, 7, 20, 1, 3, 4, 8, 18]
list_data3 = [1, 2, 3]
list_of_zero = [0, 0, 0]
str_data = [5, 4, 3, 2, 1, "test"]
float_data = [1.0, 3.5, 9.1, 2.7, 8.2]
empty_data = []


def test_mean_1():
    assert(mean(empty_data) == -1)

def test_mean_2():
    assert(mean(list_data) == 6)

def test_mean_3():
    assert(mean(list_data2) == 7)


def test_median_1():
    assert(median(empty_data) == -1)

def test_median_2():
    assert(median(list_data3) == 2)

def test_median_3():
    assert(median(list_data) == 5)


# Value frequencies - value:frequency
# Empty list, ans = []
def test_mode_1():
    assert(mode(empty_data) == [])

# 0:1, 1:1, 2:1, 4:2, 5:1, 6:1, 7:1, 8:1, 9:1, 20:1, ans = [4]
def test_mode_2():
    assert(mode(list_data) == [4])

# 1:1, 2:2, 3:1, 4:2, 5:1, 6:1, 7:1, 8:1, 9:1, 18:1, 20:1, ans = [2,4]
def test_mode_3():
    assert(mode(list_data2) == [2, 4])

# List of zeros
# 0:3, ans = [0]
def test_mode_4():
    assert(mode(list_of_zero) == [0])

# String in list, ans = ValueError
def test_mode_valueError():
    with pytest.raises(ValueError) as error : mode(str_data)
    assert("List contains non integer value" == str(error.value))


def test_range_1():
    assert(range(empty_data) == -1)

def test_range_2():
    assert(range(list_data) == 20)

def test_range_3():
    assert(range(list_data2) == 19)


# Sorted list = [0, 1, 2, 4, 4, 5, 6, 7, 8, 9, 20]
# Split = [0, 1, 2, 4, 4] [6, 7, 8, 9, 20]
# Split lower half = [0, 1] 2 [4, 4] , ans = 2
def test_lowerquartile_1():
    assert(lower_quartile(list_data) == 2)

# Sorted list = [1, 2, 2, 3, 4, 4, 6, 7, 8, 9, 18, 20]
# Split = [1, 2, 2, 3, 4, 4] [6, 7, 8, 9, 18, 20]
# Split lower half = [1, 2] 2, 3 [4, 4], ans = (2+3)/2 = 2.5
def test_lowerquartile_2():
    assert(lower_quartile(list_data2) == 2.5)

# Empty list, ans = -1
def test_lowerquartile_3():
    assert(lower_quartile(empty_data) == -1)

# Float in list, ans = ValueError
def test_lowerquartile_valueError():
    with pytest.raises(ValueError) as error : lower_quartile(float_data)
    assert("List contains non integer value" == str(error.value))

# String in list, ans = ValueError
def test_lowerquartile_valueError2():
    with pytest.raises(ValueError) as error : lower_quartile(str_data)
    assert("List contains non integer value" == str(error.value))


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

# list of length 3, ans = -1
def test_upperquartile_3():
    assert(upper_quartile(list_data3) == -1)


# sum = 66, elements = 11, mean = 6, ans = 296/11
def test_variance_1():
    assert(variance(list_data) == round(296/11, 3))

# sum = 84, elements = 12, mean = 7, ans = 416/12 = 104/3
def test_variance_2():
    assert(variance(list_data2) == round(104/3, 3))

# sum = 0, elements = 0, ans = -1
def test_variance_3():
    assert(variance(empty_data) == -1)



def test_standard_deviation_1():
    assert(standard_Deviation(empty_data) == -1)

def test_standard_deviation_2():
    assert(standard_Deviation(list_data) == round(math.sqrt(296/11),3))

def test_standard_deviation_3():
    assert(standard_Deviation(list_data2) == round(math.sqrt(104/3),3))


