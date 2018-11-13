"""
------------------------------------------------------------------------------------------------------------------------
Name: statTools.py
Purpose:
    Library of Statistical Functions for Measures of Central Tendencies and Measures of Spread for
    Includes : mean, median, mode, range, upper quartile, lower quartile, variance and standard deviation
Author: Tang.C, Ni.T
Created: 2018/11/11
------------------------------------------------------------------------------------------------------------------------
"""
import math
def not_int_list(list_data: list) -> bool:
    ''' Determine if list contains non integer value
    :param list_data: list of values
    :return: bool, True if list contains non int, otherwise False
    Author: Tang.C
    '''
    # Loop through list
    for value in list_data:
        # Return true if the value is not int
        if not isinstance(value, int):
            return True
    return False

def mean(list_data: list) -> float:
    ''' Returns mean of list
    :param list_data: list of values
    :return: float, mean of the list
    Author: Ni.T
    '''
    # Handle non list input
    if not isinstance(list_data, list): raise TypeError("Not list")
    # Empty list exception
    if len(list_data) == 0: return -1
    # List contains value that is not int
    if not_int_list(list_data): raise ValueError("List contains non integer value")
    return sum(list_data) / len(list_data)

def median(list_data: list) -> float:
    ''' Returns median of list
    :param list_data: list of values
    :return: float, median of the list
    Author: Ni.T
    '''
    # Handle non list input
    if not isinstance(list_data, list): raise TypeError("Not list")
    # Empty list exception
    if len(list_data) == 0: return -1
    # List contains value that is not int
    if not_int_list(list_data): raise ValueError("List contains non integer value")
    list_data.sort()
    divider = len(list_data) // 2
    if len(list_data) % 2 == 0:
        return (list_data[divider - 1] + list_data[divider]) / 2
    else:
        return list_data[divider]

def mode(list_data: list) -> list:
    # List of values to return
    ret_mode = []
    # Handle exception if list_data is not a list
    if not isinstance(list_data, list): raise TypeError("Not list")
    # Handle exception if list_data contains non int
    if not_int_list(list_data): raise ValueError("List contains non integer value")
    # Occurences of each value in list_data
    freq = {}
    # Maximum occurence of a value
    mx = 0
    for num in list_data:
        # Hash num if not accounted for yet
        if num not in freq:
            freq[num] = 0
        # Increase occurence by 1
        freq[num] += 1
        mx = max(mx, freq[num])
    # Iterate through keys, add all numbers with same frequency as maximum
    for num, value in freq.items():
        if value == mx:
            ret_mode.append(num)
    ret_mode.sort()
    return ret_mode

def range(list_data: list) -> float:
    ''' Returns range of list
    :param list_data: list of values
    :return: float, range of the list
    Author: Ni.T
    '''
    # Handle non list input
    if not isinstance(list_data, list): raise TypeError("Not list")
    # Empty list exception
    if len(list_data) == 0: return -1
    # List contains value that is not int
    if not_int_list(list_data): raise ValueError("List contains non integer value")
    list_data.sort()
    return list_data[len(list_data) - 1] - list_data[0]

def lower_quartile(list_data: list) -> int:
    ''' Returns lower quartile of a list
        Lower quartile : median of lower half of list
    :param list_data: list of values
    :return: int, lower quartile of list
    Author: Tang.C
    '''
    # Handle non list input
    if not isinstance(list_data, list) : raise TypeError("Not list")
    # Handle list that is less than 4 values, no lower quartile, returns -1
    if len(list_data) < 4 : return -1
    # Handle non int in list
    if not_int_list(list_data) : raise ValueError("List contains non integer value")

    list_data.sort()
    # Create list consisting of lower half of list_data
    list_lowerhalf = list_data[:len(list_data)//2]
    # Even value count in list_data, even value count in lower half of list
    # Find median for even/odd list
    if len(list_data) % 2 == 0 :
        return (list_lowerhalf[len(list_lowerhalf)//2 - 1] + list_lowerhalf[len(list_lowerhalf)//2]) / 2
    else :
        return list_lowerhalf[len(list_lowerhalf)//2]

def upper_quartile(list_data: list) -> int:
    ''' Return upper quartile of a list
        Upper quartile : median of upper half of list
    :param list_data: list of values
    :return: int, upper quartile of list
    Author: Tang.C
    '''
    # Handle non list input
    if not isinstance(list_data, list) : raise TypeError("Not list")
    # Handle list that is less than 4 values, no upper quartile, returns -1
    if len(list_data) < 4 : return -1
    # Handle non int in list
    if not_int_list(list_data) : raise ValueError("List contains non integer value")

    list_data.sort()
    # Create list consisting of upper half of list_data
    list_upperhalf = list_data[len(list_data)//2:]
    # Even value count in list_data, even value count in upper half of list
    # Find median for even/odd list
    if len(list_data) % 2 == 0 :
        return (list_upperhalf[len(list_upperhalf)//2 - 1] + list_upperhalf[len(list_upperhalf)//2]) / 2
    else :
        return list_upperhalf[len(list_upperhalf)//2]

def variance(list_data: list) -> float:
    ''' Return variance of a list
        Variance : Spread of numbers from the average value in the list
    :param list_data: list of values
    :return: float, variance of the list rounded to 3 decimals
    Author: Tang.C
    '''
    # Handle non list input
    if not isinstance(list_data, list) : raise TypeError("Not list")
    # Empty list exception
    if len(list_data) == 0 : return -1
    # List contains value that is not int
    if not_int_list(list_data) : raise ValueError("List contains non integer value")
    # Find mean of list
    mean = sum(list_data) / len(list_data)
    total = 0
    # Find difference of each number in list to the mean
    for num in list_data:
        # Add difference squared to total
        total += abs(mean-num) * abs(mean-num)
    # Divide total by list length and round to 3 decimals
    return round(total / len(list_data), 3)

def standard_Deviation(list_data: list) -> float:
    ''' Returns standard deviation of list
        Standard Deviation: the square root of the spread of numbers from the average value in the list
    :param list_data: list of values
    :return: float, standard deviation of the list rounded to 3 decimals
    Author: Ni.T
    '''
    # Handle non list input
    if not isinstance(list_data, list): raise TypeError("Not list")
    # Empty list exception
    if len(list_data) == 0: return -1
    # List contains value that is not int
    if not_int_list(list_data): raise ValueError("List contains non integer value")
    mean = sum(list_data) / len(list_data)
    total = 0
    for num in list_data:
        total += abs(mean - num) * abs(mean - num)
    return round(math.sqrt(total / len(list_data)), 3)