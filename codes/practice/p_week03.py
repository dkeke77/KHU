from assist import rand_func

def bs(data, item, low, high):
    result = -1
    if low > high:
        return result
    else:
        mid = (low+high)//2
        if item == data[mid]:
            return mid
        elif item < data[mid]:
            high = mid - 1
            result = bs(data, item, low, high)
        else:
            low = mid + 1
            result = bs(data, item, low, high)
    return result

def mergeSort(n, s):
    if n > 1:
        s_l = s[:n//2]
        s_r = s[n//2:]
        h = len(s_l)
        m = len(s_r)
        s_l = mergeSort(h,s_l)
        s_r = mergeSort(m,s_r)
        return merge(h,m,s_l,s_r,s)
    else:
        return s

def merge(h, m, u, v, s):
    i,j,k = 0,0,0
    while(j < h and k < m):
        if u[j] < v[k]:
            s[i] = u[j]
            j += 1
        else:
            s[i] = v[k]
            k += 1
        i += 1

    if j < h:
        s[i:] = u[j:]
    else:
        s[i:] = v[k:]

    return s

data=[1,3,5,6,7,9,10,14,17,19]
n=10
print("binary search")
location=bs(data,17,0,n-1)
print(location, end="\n\n")

print("merge sort")
s=[3,5,2,9,10,14,4,8]
print(mergeSort(8,s))