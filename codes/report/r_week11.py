# 부분집합의 합 문제
print("==== 부분집합의 합 ====")
def sos_promising(i,weight, total):
    return (weight + total >= W) and (weight == W or weight + w[i+1] <= W)

def sum_of_subsets(i, weight, total, include):
    global nodes_count
    nodes_count += 1
    if sos_promising(i, weight, total):
        if weight == W:
            print("sol",include)
        else:
            i += 1
            include[i] = 1
            sum_of_subsets(i,weight+w[i],total-w[i],include)
            include[i] = 0
            sum_of_subsets(i,weight,total-w[i],include)

nodes_count = 0
w=[2,3,5,7,8]
W=8
print("items =",w, "W =", W)
include = len(w)*[0]
total=0
for k in w:
    total+=k
sum_of_subsets(-1,0,total,include)
print("총 노드 개수 :",nodes_count,end="\n\n")


# m-coloring 문제
print("==== m-coloring ====")
def color(i,vcolor):
    global nodes_count
    nodes_count += 1
    if col_promising(i,vcolor):
        if i+1 == n :
            print(vcolor)
            global is_solved
            is_solved = True
        else:
            i+=1
            for j in range(1,m+1):
                vcolor[i] = j
                color(i, vcolor)
            vcolor[i] = 0

def col_promising(i,vcolor):
    switch = True
    j = 0
    while (switch and j < i):
        if (G[i][j] == 1 and vcolor[i] == vcolor[j]):
            switch = False
        j += 1
    return switch

G=[[0,1,0,1,0,0],
   [1,0,1,0,1,0],
   [0,1,0,0,1,0],
   [1,0,0,0,1,1],
   [0,1,1,1,0,1],
   [0,0,0,1,1,0]]
nodes_count = 0
n=len(G[0])
vcolor=n*[0]
is_solved = False
for m in range(2,5):
    color(-1,vcolor)
    if is_solved : break
print("총 노드 개수 :",nodes_count)