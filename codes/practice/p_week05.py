import time

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

t1 = time.time()
print(bin(10,5) end="")
t1 = (time.time() - t1)*1000

t2 = time.time()
print(bin(10,5))
t2 = (time.time() - t2)*1000

print("{0:0.2f}ms {1:0.2f}ms".format(t1, t2))