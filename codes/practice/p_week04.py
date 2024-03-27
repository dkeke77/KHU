import numpy as np

def strassen(n, A, B, C):
    if(n<=2):
        C = np.array(A)@np.array(B)
    else:
        A_sp = []
        B_sp = []
        half = n//2

        for i in range(2):
            for j in range(2):
                A_sp.append(np.array([[A[rows][cols] for cols in range(half*j,half*(j+1))]for rows in range(half*i,half*(i+1))]))
                B_sp.append(np.array([[B[rows][cols] for cols in range(half*j,half*(j+1))]for rows in range(half*i,half*(i+1))]))
        
        M1 = M2 = M3 = M4 = M5 = M6 = M7 = np.array([])
        M1 = strassen(half, A_sp[0]+A_sp[3], B_sp[0]+B_sp[3], M1)
        M2 = strassen(half, A_sp[2]+A_sp[3], B_sp[0], M2)
        M3 = strassen(half, A_sp[0], B_sp[1]-B_sp[3], M3)
        M4 = strassen(half, A_sp[3], B_sp[2]-B_sp[0], M4)
        M5 = strassen(half, A_sp[0]+A_sp[1], B_sp[3], M5)
        M6 = strassen(half, A_sp[2]-A_sp[0], B_sp[0]+B_sp[1], M6)
        M7 = strassen(half, A_sp[1]-A_sp[3], B_sp[2]+B_sp[3], M7)

        C = np.vstack([ np.hstack([M1+M4-M5+M7, M3+M5]), np.hstack([M2+M4, M1+M3-M2+M6]) ])
    
    return C

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
D = np.array([[0 for cols in range(n)]for rows in range(n)])
print(C)
D = strassen(n,A,B,D)
print(D)