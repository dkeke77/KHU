import utility

# 문제1 : 최적이진검색트리
class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data = data

def tree(key,r,i,j):
    k=r[i][j]
    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child=tree(key,r,i,k-1)
        p.r_child=tree(key,r,k+1,j)
    return p

# 값 설정
key=[" ","A","B","C","D","E"]
p=[0,3/16,4/16,2/16,6/16,1/16]
n=len(p)-1

a=[[0 for j in range(0,n+2)] for i in range(0,n+2)]
r=[[0 for j in range(0,n+2)] for i in range(0,n+2)]

for i in range (1,n+1):
    a[i][i-1]=0
    a[i][i]=p[i]
    r[i][i]=i
    r[i][i-1]=0
a[n+1][n]=0
r[n+1][n]=0

# 문제1 알고리즘 구현
for diagonal in range(1,n):
    for i in range(1,n-diagonal+1):
        j = i + diagonal
        min_a = a[i][i-1] + a[i+1][j]
        min_k = i

        for k in range(i+1,j+1):
            if min_a > a[i][k-1] + a[k+1][j]:
                min_a = a[i][k-1] + a[k+1][j]
                min_k = k
        
        a[i][j] = min_a + sum(p[i:j+1])
        r[i][j] = min_k

print("===== Problem 1 =====")
utility.printMatrixF(a)
print()
utility.printMatrix(r)

root=tree(key,r,1,n)
utility.print_inOrder(root)
print()
utility.print_preOrder(root)
print("\n\n")

# 문제 2 : DNA 서열 맞춤 알고리즘
a=['A','C','G','A','C','T']
b=['C','C','G','A','T','C','T']

m=len(a)
n=len(b)
table=[[0 for j in range(0,n+1)] for i in range(0,m+1)]
minindex = [[ (0,0) for j in range(0,n+1)] for i in range(0,m+1)]

for j in range(n-1,-1,-1):
    table[m][j] =table[m][j+1]+2

for i in range(m-1,-1,-1):
    table[i][n] =table[i+1][n]+2

# 문제2 알고리즘 구현
i,j = m-1,n-1
for t in range(m+n+1):
    print(t)
    while(i<m and j>=0):
        penalty = 1
        if a[i] == b[j] :
            penalty = 0
        values = [table[i+1][j+1]+penalty,table[i+1][j]+2,table[i][j+1]+2]
        min_value = min(values)
        table[i][j] = min_value
        
        if min_value == values[0]:
            minindex[i][j] = (i+1,j+1)
        elif min_value == values[1]:
            minindex[i][j] = (i+1,j)
        else:
            minindex[i][j] = (i+1,j)

        i += 1
        j -= 1

    if t <= m:
        i,j = m-t-1,n-1
    else :
        i,j = 0,n-(t-m)-1

print("===== Problem 2 =====")
utility.printMatrix(table)
x=0
y=0

while (x <m and y <n):
    tx, ty = x, y
    print(minindex[x][y])
    (x,y)= minindex[x][y]
    if x == tx + 1 and y == ty+1:
        print(a[tx]," ", b[ty])
    elif x == tx and y == ty+1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " " , " -")
