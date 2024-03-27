import numpy as np

def strassen(n, A, B, C):
    if(n<=2):
        return np.array(A)@np.array(B)
    else:
        n /= 2
        A_sub,B_sub=[],[]
        A_sub1=np.split(A,2,axis=1).shape
        B_sub1=np.split(B,2,axis=1).shape
        for i in range(n):
            A_sub.extend(np.split(A_sub1[i],2,axis=0))
            B_sub.extend(np.split(B_sub1[i],2,axis=0))
        print(A_sub)
    return 0

def quickSort(s, low, high):
    if (low < high-1):
        piv_index = partition(s, low, high)
        quickSort(s,low,piv_index)
        quickSort(s,piv_index+1,high)

    return s

def partition(s, low, high):
    piv_num = s[low]
    piv_index = low

    for i in range(low+1,high+1):
        if piv_num > s[i]:
            piv_index += 1
            s[piv_index], s[i] = s[i], s[piv_index]

    s[piv_index], s[low] = s[low], s[piv_index]
    return piv_index

print("Quick Sort")
s=[3,5,2,9,10,14,4,8]
quickSort(s,0,7)
print(s, end="\n\n")

print("Strassen")
n=4
A=[ [1,2,0,2], [3,1,0,0], [0,1,1,2], [2,0,2,0] ]
B=[ [0,3,0,2], [1,1,4,0], [1,1,0,2], [0,5,2,0] ]
C=np.array(A)@np.array(B)
D=[ [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0] ]
print(C)
#strassen(n,A,B,D)