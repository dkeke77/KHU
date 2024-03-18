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

def merge_sort_gpt(arr):
    length = len(arr)
    if length <= 1:
        return arr

    mid = length // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort_gpt(left)
    right = merge_sort_gpt(right)

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 요소들을 추가
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

sample = 50000

print("selection sort : " + tester.tester_rand_rep(sel_sort,sample,3))
print("merge sort     : " + tester.tester_rand_rep(merge_sort,sample,3))
print("merge sort new : " + tester.tester_rand_rep(merge_sort_gpt,sample,3))