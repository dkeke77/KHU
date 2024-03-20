from assist import rand_func

#Sequence Search
def seqsearch(s, x):
    for i in range(len(s)):
        if s[i] == x:
            return i
    return -1

#Exchange Sort
def exchangesort(s):
    for i in range(len(s)-1):
        for j in range(i,len(s)):
            if(s[i]>s[j]):
                s[i], s[j] = s[j], s[i]

    return s

#main
arr1 = rand_func.rand_num_list(21,0)
loc = seqsearch(arr1, 20)
print("Sequence Search")
print(arr1)
print(loc)

arr2 = rand_func.rand_num_list(10,0)
print("Exchange Sort")
print(arr2)
print(exchangesort(arr2))