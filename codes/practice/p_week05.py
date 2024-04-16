import time
import utility as util

def bin(n,k):
    #recursive
    if (k == 0 or n == k):
        return 1
    else:
        return bin(n-1,k-1) + bin(n-1,k)

def bin2(n,k):
    #array
    i = j = 0
    arr = [[0 for j in range(k+1)] for i in range(n+1)]
    
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    return arr[n][k]

def allShortestPath(g,n):
    ln = len(g)
    D = g
    P = [[0 for j in range(ln)] for i in range(ln)]

    for k in range(ln):
        for i in range(ln):
            for j in range(ln):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k+1
    return D, P

def path(p, q, r):
    if (p[q-1][r-1] !=0):
        path(p, q, p[q-1][r-1])
        print("v{0}".format(p[q-1][r-1]), end=" ")
        path(p, p[q-1][r-1], r)

def printMatrix(d):
    n=len(d[0])
    for i in range(0,n):
        for j in range(0,n):
            print(d[i][j],end=" ")
        print()

def minmult(d, n):
    m = [[0 for j in range(1,n+2)] for i in range(1,n+2)]
    p = [[0 for j in range(1,n+2)] for i in range(1,n+2)]

    for diagonal in range(1,n):
        for i in range(1,n-diagonal+1):
            j = diagonal+i
            for k in range(i,j):
                new = m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
                if m[i][j] > new or m[i][j] == 0:
                    m[i][j] = new
                    p[i][j] = k

    return m, p

def order(p,i,j):
    if i == j:
        print("A{0}".format(i), end="")
    else:
        print("(",end="")
        order(p,i,p[i][j])
        order(p,p[i][j]+1,j)
        print(")",end="")

# binomial coefficient
t1 = time.time()
#print(bin(10,5), end=" ")
t1 = (time.time() - t1)*1000

t2 = time.time()
#print(bin(10,5))
t2 = (time.time() - t2)*1000

#print("{0:0.2f}ms {1:0.2f}ms".format(t1, t2))

# Floyd
print("Floyd Algorithm")
inf=1000
g=[[0,1,inf, 1,5],
    [9,0,3,2,inf],
    [inf,inf,0,4,inf],
    [inf,inf,2,0,3],
    [3,inf,inf,inf,0]]

d, p = allShortestPath(g,5)
print()
printMatrix(d)
print()
printMatrix(p)
path(p, 5, 3)
print("\n\n")

#Minimum Multiplication
print("Minimum Multiplication")
d=[5,2,3,4,6,7,8]
n=len(d)-1

m,p = minmult(d,n)
util.printMatrix(m)
print()
util.printMatrix(p)
order(p,1,6)