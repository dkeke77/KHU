def promising(i,col):
    switch = True
    for j in range(i):
        if (col[i] == col[j] or abs(col[i] - col[j]) == (i - j)):
            switch = False
            break
    return switch

def queens_old(n,i,col):
    global node_count_old
    node_count_old += 1
    if promising(i,col):
        if i == n-1:
            solutions_o.append(col.copy())
        else:
            i += 1
            for j in range(n):
                col[i] = j
                queens_old(n,i,col)

def queens_new(n,i,col):
    global node_count_new
    node_count_new += 1
    i += 1
    for j in range(n):
        col[i] = j
        if promising(i,col):
            if i == n-1:
                solutions_n.append(col.copy())
            else:
                queens_new(n,i,col)

node_count_old = 0
node_count_new = 0
n=8

solutions_o = []
col=n*[0]
queens_old(n,-1,col)

solutions_n = []
col=n*[0]
queens_new(n,-1,col)

print(solutions_o == solutions_n)
print("기존 알고리즘 총 노드 수 :", node_count_old)
print("개선 알고리즘 총 노드 수 :", node_count_new)