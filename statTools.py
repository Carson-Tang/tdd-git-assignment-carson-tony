def mode(list_data):
    if len(list_data) == 0 : return None
    freq = {}
    mx = 0
    for num in list_data:
        if num not in freq:
            freq[num]=0
        freq[num]+=1
        mx = max(mx,freq[num])
    mode = []
    for num,value in freq.items():
        if value==mx:
            mode.append(num)
    if len(mode) == 1 : return mode[0]
    mode.sort()
    return mode