def mode(list_data: list) -> list:
    ''' Returns mode of list

    :param list_data: list of values
    :return: list of most frequent values
    '''
    # list to return
    mode = []
    # map of frequency of each value
    freq = {}
    # max occurrences of a value
    mx = 0
    # empty list handling
    if len(list_data) == 0 : return mode
    for num in list_data:
        # hash num if not put in freq map
        if num not in freq:
            freq[num] = 0
        # increase value frequency
        freq[num] += 1
        # update max occurrences
        mx = max(mx, freq[num])
    # add values to return list if they have same occurrence as max occurrences
    for num, value in freq.items():
        if value == mx:
            mode.append(num)
    mode.sort()
    return mode

def lower_quartile(list_data):
    if len(list_data) == 0 : return None
    if len(list_data) < 4 : return 0
    list_data.sort()
    list_lowerhalf = list_data[:len(list_data)//2]
    if len(list_data) % 2 == 0 :
        return (list_lowerhalf[len(list_lowerhalf)//2 - 1] + list_lowerhalf[len(list_lowerhalf)//2]) / 2
    else :
        return list_lowerhalf[len(list_lowerhalf)//2]

def upper_quartile(list_data):
    if len(list_data) == 0 : return None
    if len(list_data) < 4 : return 0
    list_data.sort()
    list_upperhalf = list_data[len(list_data)//2:]
    if len(list_data) % 2 == 0 :
        return (list_upperhalf[len(list_upperhalf)//2 - 1] + list_upperhalf[len(list_upperhalf)//2]) / 2
    else :
        return list_upperhalf[len(list_upperhalf)//2]

def variance(list_data):
    if len(list_data) == 0 : return None
    mean = sum(list_data) / len(list_data)
    total = 0
    for num in list_data:
        total += abs(mean-num) * abs(mean-num)
    return round(total / len(list_data),3)