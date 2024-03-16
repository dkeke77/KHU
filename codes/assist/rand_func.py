import random

def rand_num_list(length, min, max):
    result = list()
    if length > max - min + 1:
        return result
    result.append(random.randint(min,max))
    for i in range(length-1):
        k = random.randint(min,max)
        while(1):
            temp=k
            for j in result:
                if j == k :
                    k += 1
                    if k>max:
                        k=min
                    break
            if temp==k:
                break
        result.append(k)
    return result