import assist.tester as tester
import time
       
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
    if length > 1:
        result = []
        arr1 = arr[:length//2]
        arr2 = arr[length//2:]
        arr1, arr2 = merge_sort(arr1), merge_sort(arr2)
        i,j=0,0
        while(i+j<length):
            if len(arr1) == i:
                result += arr2[j:]
                break
            elif len(arr2) == j:
                result += arr1[i:]
                break
            elif arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        return result
    else:
        return arr

print("selection sort : " + tester.tester_rand_rep(sel_sort,5000,3))
print("merge sort     : " + tester.tester_rand_rep(merge_sort,5000,3))