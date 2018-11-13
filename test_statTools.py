"""
------------------------------------------------------------------------------------------------------------------------
Name: test_statTools.py
Purpose:
    Tests for Functions of Measures of Central Tendencies and Measures of Spread

Author: Tang.C, Ni.T
Created: 2018/11/11
------------------------------------------------------------------------------------------------------------------------
"""
import pytest
from statTools import *

# Different lists to test various cases
# Odd number of values
list_data = [0, 9, 6, 2, 4, 7, 20, 1, 5, 4, 8]
# Even number of values
list_data2 = [2, 9, 6, 2, 4, 7, 20, 1, 3, 4, 8, 18]
# List of 3 values
list_data3 = [1, 2, 3]
# List of 0's
list_of_zero = [0, 0, 0]
# List that contains a string
str_data = [5, 4, 3, 2, 1, "test"]
# List that contains floats
float_data = [1.0, 3.5, 9.1, 2.7, 8.2]
# Empty list
empty_data = []
# Negative number in list
neg_num_data = [-1, -5, -10]
# Non list
number = 10

##### Mean #####
# [0, 1, 2, 4, 4, 5, 6, 7, 8, 9, 20] , ans = 6
def test_mean_1():
    assert(mean(list_data) == 6)

# [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 18, 20] , ans = 7
def test_mean_2():
    assert(mean(list_data2) == 7)

# [] , ans = -1
def test_mean_3():
    assert(mean(empty_data) == -1)

# [0, 0, 0] , ans = 0
def test_mean_4():
    assert(mean(list_of_zero) == 0)

# [-1, -5, -10] , ans = -5.33
def test_mean_5():
    assert(mean(neg_num_data) == -5.33)

# Float in list, ans = ValueError
def test_mean_valueError():
    with pytest.raises(ValueError) as error : mean(float_data)
    assert("List contains non integer value" == str(error.value))

# Number passed in function instead of list
def test_mean_typeError():
    with pytest.raises(TypeError) as error : mean(number)
    assert("Not list" == str(error.value))

##### Median #####
# [] , ans = -1
def test_median_1():
    assert(median(empty_data) == -1)

#[1, 2, 3], ans = 2
def test_median_2():
    assert(median(list_data3) == 2)

# [0, 1, 2, 4, 4, 5, 6, 7, 8, 9, 20] , ans = 5
def test_median_3():
    assert(median(list_data) == 5)

# [0, 0, 0] , ans = 0
def test_median_4():
    assert(median(list_of_zero) == 0)

# [-1, -5, -10] , ans = -5
def test_median_5():
    assert(median(neg_num_data) == -5)

# Float in list, ans = ValueError
def test_Median_valueError():
    with pytest.raises(ValueError) as error : median(float_data)
    assert("List contains non integer value" == str(error.value))

# Number passed in function instead of list
def test_Median_typeError():
    with pytest.raises(TypeError) as error : median(number)
    assert("Not list" == str(error.value))

##### Mode #####

# [] , ans = []
def test_mode_1():
    assert(mode(empty_data) == [])

# [0, 1, 2, 4, 4, 5, 6, 7, 8, 9, 20] , ans = [4]
def test_mode_2():
    assert(mode(list_data) == [4])

# [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 18, 20] , ans = [2,4]
def test_mode_3():
    assert(mode(list_data2) == [2, 4])

# [0, 0, 0] , ans = [0]
def test_mode_4():
    assert(mode(list_of_zero) == [0])

# [-1, -5, -10] , ans = [-10, -5, -1]
def test_mode_5():
    assert(mode(neg_num_data) == [-10, -5, -1])

# String in list, ans = ValueError
def test_mode_valueError():
    with pytest.raises(ValueError) as error : mode(str_data)
    assert("List contains non integer value" == str(error.value))

# Number passed in function instead of list
def test_mode_typeError():
    with pytest.raises(TypeError) as error : mode(number)
    assert("Not list" == str(error.value))


##### Range #####
# [], ans = -1
def test_range_1():
    assert(range(empty_data) == -1)

# [0, 1, 2, 4, 4, 5, 6, 7, 8, 9, 20] , ans = 20
def test_range_2():
    assert(range(list_data) == 20)

# [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 18, 20] , ans = 19
def test_range_3():
    assert(range(list_data2) == 19)

# [0, 0, 0] , ans = 0
def test_range_4():
    assert(range(list_of_zero) == 0)

# [-1, -5, -10] , ans = 9
def test_range_5():
    assert(range(neg_num_data) == 9)

# Float in list, ans = ValueError
def test_Range_valueError():
    with pytest.raises(ValueError) as error : range(float_data)
    assert("List contains non integer value" == str(error.value))

# Number passed in function instead of list
def test_Range_typeError():
    with pytest.raises(TypeError) as error : range(number)
    assert("Not list" == str(error.value))

##### Lower Quartile #####
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

##### Upper Quartile #####
# Sorted list = [0, 1, 2, 4, 4, 5, 6, 7, 8, 9, 20]
# Split = [0, 1, 2, 4, 4] [6, 7, 8, 9, 20]
# Split top half = [6, 7] 8 [9, 20], ans = 8
def test_upperquartile_1():
    assert(upper_quartile(list_data) == 8)

# Sorted list = [1, 2, 2, 3, 4, 4, 6, 7, 8, 9, 18, 20]
# Split = [1, 2, 2, 3, 4, 4] [6, 7, 8, 9, 18, 20]
# Split lower half = [6, 7] 8, 9 [18, 20], ans = (8+9)/2 = 8.5
def test_upperquartile_2():
    assert(upper_quartile(list_data2) == 8.5)

# List of length 3, ans = -1
def test_upperquartile_3():
    assert(upper_quartile(list_data3) == -1)

# Number passed to function instead of list
def test_upperquartile_typeError():
    with pytest.raises(TypeError) as error : upper_quartile(number)
    assert("Not list" == str(error.value))

##### Variance #####
# Sum = 66, elements = 11, mean = 6, ans = 296/11
def test_variance_1():
    assert(variance(list_data) == round(296/11, 3))

# Sum = 84, elements = 12, mean = 7, ans = 416/12 = 104/3
def test_variance_2():
    assert(variance(list_data2) == round(104/3, 3))

# Sum = 0, elements = 0, ans = -1
def test_variance_3():
    assert(variance(empty_data) == -1)

# Float in list, ans = ValueError
def test_variance_valueError():
    with pytest.raises(ValueError) as error : variance(float_data)
    assert("List contains non integer value" == str(error.value))

# String in list, ans = TypeError
def test_variance_typeError():
    with pytest.raises(TypeError) as error : variance(number)
    assert("Not list" == str(error.value))

##### Standard Deviation #####
# [], ans = -1
def test_standard_deviation_1():
    assert(standard_Deviation(empty_data) == -1)

# [0, 1, 2, 4, 4, 5, 6, 7, 8, 9, 20] , ans = 5.187
def test_standard_deviation_2():
    assert(standard_Deviation(list_data) == round(math.sqrt(296/11),3))

# [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 18, 20] , ans = 5.88
def test_standard_deviation_3():
    assert(standard_Deviation(list_data2) == round(math.sqrt(104/3),3))

# [], ans = 0
def test_standar_deviation_3():
    assert(standard_Deviation(list_of_zero) == 0)

# Float in list, ans = ValueError
def test_standar_deviation_valueError():
    with pytest.raises(ValueError) as error: standard_Deviation(float_data)
    assert ("List contains non integer value" == str(error.value))

# Number passed to function instead of list
def test_standard_deviation_typeError():
    with pytest.raises(TypeError) as error: standard_Deviation(number)
    assert ("Not list" == str(error.value))