import random

def rand_num_list(length, min=1, max=-1):
    #return NOT duplicated random int list
    if min == 1 and max == -1:
        min, max = 1, length
    elif min != 1 and max == -1:
        max = length + min - 1
    elif length <= max - min + 1:
        return []
        
    return random.sample(range(min,max+1),length)

def rand_num_list_du(length, min, max):
    #return duplicated random int list
    result = []

    if length <= max - min + 1:
        return result
    
    for i in range(0,length):
        result.append(random.randint(min,max))

    return result