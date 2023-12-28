def capital_indexes(string):
    khali = []
    lis = list(string)
    for i in range(len(lis)):
        if lis[i].isupper():
            khali.append(i)
    
    return khali


