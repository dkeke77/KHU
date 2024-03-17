import random

def rand_num_list(length, min=1, max=-1):
    if min == 1 and max == -1:
        min, max = 1, length
    elif min != 1 and max == -1:
        max = length + min - 1
    elif length <= max - min + 1:
        return []
        
    return random.sample(range(min,max+1),length)

