def promising(i,col):
    switch = True
    for j in range(i):
        if (col[i] == col[j] or abs(col[i] - col[j]) == (i - j)):
            switch = False
            break
    return switch

def queens(n,i,col):
    global node_count
    node_count += 1
    if promising(i,col):
        if i == n-1:
            solutions.append(col.copy())
        else:
            i += 1
            for j in range(n):
                col[i] = j
                queens(n,i,col)

solutions = []
node_count = 0
n=8
col=n*[0]
queens(n,-1,col)
print("해의 총 개수 :", len(solutions))
print("5번째 해 :", solutions[4])
print("생성한 상태공간트리의 총 노드 수 :", node_count)