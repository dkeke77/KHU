import heapq

# 알고리즘용 노드 클래스 구현부
class Node:
    def __init__(self,level,weight, profit, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include.copy()
        self.bound = 0
        
    def compBound(self):
        self.bound = self.profit
        weight_temp = self.weight
        if weight_temp > W:
           self.bound = 0
        else:
            for i in range(self.level+1,n):
                weight_temp += w[i]
                if (weight_temp <= W):
                    self.bound += p[i]
                else:
                    self.bound += p[i] * (W + w[i] - weight_temp)/w[i]
                    break

    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self.level, self.weight, self.profit, self.include)

# 너비우선탐색 알고리즘 구현부
def kp_Breadth_FS():
    global node_count, max_queue, bestset
    queue = []
    bestset = n*[0]
    node_count,max_queue,maxProfit = 0,0,0
    v = Node(-1,0,0,include)
    v.compBound()
    queue.append(v)
    node_count = 1

    while(len(queue) != 0):
        node_count += 2
        max_queue = max(max_queue, len(queue))
        v = queue.pop(0)

        u = Node(v.level+1,v.weight,v.profit,v.include)
        u.weight = u.weight + w[u.level]
        u.profit = u.profit + p[u.level]
        u.include[u.level] = 1
        u.compBound()

        if (u.weight <= W and u.profit > maxProfit):
            maxProfit = u.profit
            bestset = u.include.copy()
        if (u.bound > maxProfit and u.level < n-1):
            queue.append(u)

        u = Node(v.level+1,v.weight,v.profit,v.include)
        u.compBound()

        if (u.bound > maxProfit and u.level < n-1):
            queue.append(u)

# 최고우선탐색 알고리즘 구현부
def kp_Best_FS():
    global node_count, max_queue, bestset
    queue = []
    bestset = n*[0]
    node_count,max_queue,maxProfit = 0,0,0
    v = Node(-1,0,0,include)
    v.compBound()
    heapq.heappush(queue,(-v.bound,v))
    node_count = 1

    while(len(queue) != 0):
        max_queue = max(max_queue, len(queue))
        _,v =  heapq.heappop(queue)
        if (v.bound > maxProfit):
            node_count += 2
            u = Node(v.level+1,v.weight,v.profit,v.include)
            u.weight = u.weight + w[u.level]
            u.profit = u.profit + p[u.level]
            u.include[u.level] = 1
            u.compBound()
            
            if (u.weight <= W and u.profit > maxProfit):
                maxProfit = u.profit
                bestset = u.include.copy()
            if (u.bound > maxProfit and u.level < n-1):
                heapq.heappush(queue,(-u.bound,u))

            u = Node(v.level+1,v.weight,v.profit,v.include)
            u.compBound()

            if (u.bound > maxProfit and u.level < n-1):
                heapq.heappush(queue,(-u.bound,u))

n=4
W=6
p=[12,12,18,2]
w=[2,3,6,1]
include=[0]*n
global bestset, node_count, max_queue

print("===== 너비우선탐색 =====")
kp_Breadth_FS()
print("해답 : ", bestset)
print("생성된 노드 수 : ",node_count)
print("최대 큐 길이 : ",max_queue,'\n')


print("===== 최고우선탐색 =====")
kp_Best_FS()
print("해답 : ", bestset)
print("생성된 노드 수 : ",node_count)
print("최대 큐 길이 : ",max_queue,'\n')