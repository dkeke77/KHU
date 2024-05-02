# Dijkstra 알고리즘 결과 출력용 함수
def convert_node_name(num):
    return chr(97+num)

def trace_node(touch, target):
    if touch[target] != 0 :
        trace_node(touch, touch[target])
    else :
        print("a",end="")
    print(" ->",convert_node_name(target), end="")

# Dijkstra 알고리즘 변수 선언 및 초기화
inf=1000
w =[[0,3,2,8,inf,inf],
    [inf,0,1,inf,5,inf],
    [inf,inf,0,5,3,inf],
    [inf,inf,inf,0,3,2],
    [inf,inf,inf,inf,0,1],
    [inf,inf,inf,inf,inf,0]]
n=len(w[0])
f=set()
touch=n*[0]
length=n*[0]
save_length=n*[0]

for i in range(1,n):
    length[i]=w[0][i]
    save_length[i]=w[0][i]

# Dijkstra 알고리즘 구현부
for i in range(1,n):
    min = inf
    vnear = 0

    for j in range(1,n):
        if 0 < length[j] < min:
            min = length[j]
            vnear = j

    f.add((touch[vnear],vnear))

    for j in range(1,n):
        if (length[vnear] + w[vnear][j]) < length[j]:
            length[j] = length[vnear] + w[vnear][j]
            save_length[j] = length[j]
            touch[j] = vnear
    length[vnear] = -1

# 노드별 최단 경로 및 최단 거리 출력
print("노드별 최단 거리 및 최단 경로 출력")
for i in range(1,n):
    print(" {0}({1}) : ".format(convert_node_name(i),save_length[i]),end="")
    trace_node(touch,i)
    print()
print()

# 최단 거리 노드 및 최장 거리 노드 출력
print("최단 거리 노드 및 최장 거리 노드 출력")
node_near,node_far = 1,1
for i in range(1,n):
    if save_length[node_far] < save_length[i]:
        node_far = i
    if save_length[node_near] > save_length[i]:
        node_near = i

print(" 최단 거리 노드 : {0}({1})".format(convert_node_name(node_near),save_length[node_near]))
print(" 최장 거리 노드 : {0}({1})".format(convert_node_name(node_far),save_length[node_far]))