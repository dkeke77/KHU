from assist import tester
       
def sel_sort(arr):
    for i in range(len(arr)-1):
        num_min = i
        for j in range(i+1,len(arr)):
            if arr[num_min] > arr[j]:
                num_min = j
            arr[i], arr[num_min] = arr[num_min], arr[i]
    return arr

def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr

    mid = length // 2
    arr_l = arr[:mid]
    arr_r = arr[mid:]

    arr_l = merge_sort(arr_l)
    arr_r = merge_sort(arr_r)

    result = []
    i,j = 0,0

    while i < len(arr_l) and j < len(arr_r):
        if arr_l[i] < arr_r[j]:
            result.append(arr_l[i])
            i += 1
        else:
            result.append(arr_r[j])
            j += 1

    result.extend(arr_l[i:])
    result.extend(arr_r[j:])
    
    return result


#sample = [5000,10000,15000,20000,30000,40000,80000]

#for i in range(0,6):   
#    print("CASE -",sample[i])
#    print("selection sort : " + tester.tester_rand_rep_du(sel_sort,sample[i],5))
#    print("merge sort     : " + tester.tester_rand_rep_du(merge_sort,sample[i],20))
#    print("")

#print("CASE -",sample[6])
#print("merge sort     : " + tester.tester_rand_rep_du(merge_sort,sample[6],20))