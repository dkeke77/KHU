import heapq

def dijkstra(W,start):
    n = len(W[0])
    F = set()
    touch = [start] * n
    length = W[start]
    length_save = [0] * n
    length[start] = 0

    for i in range(n):
        if i == start : continue

        min = 1000
        vnear = 0

        for j in range(n):
            if 0 < length[j] < min:
                min = length[j]
                vnear = j
        
        F.add((touch[vnear],vnear))

        for j in range(n):
            if j == start : continue
            if (min + W[vnear][j]) < length[j]:
                length[j] = min + W[vnear][j]
                touch[j] = vnear
                length_save[j] = length[j]
        
        
        length[vnear] = -1

    def dijkstra_track(touch, now, dest):
        result = ""
        if touch[dest] != now:
            result += dijkstra_track(touch, now, touch[dest])
        else:
            result = "v{0}".format(now)
        return result + " -> v{0}".format(dest)
    
    print(F)
    for i in range(n):
        if i == start : continue
        print("v{0}({1}) : ".format(i, length_save[i]), end="")
        print(dijkstra_track(touch, start, i))

    return F

def Huffman_code():
    pass

# 데이크스트라 알고리즘
inf = 1000
w = [[0,7,4,6,1],
     [inf,0,inf,inf,inf],
     [inf,2,0,5,inf],
     [inf,3,inf,0,inf],
     [inf,inf,inf,1,0]]
print("Dijkstra Algorithm")
dijkstra(w,0)
print("")


#허프만 코드
