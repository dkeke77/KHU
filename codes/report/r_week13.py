import math

class Heap(object):
    n=0
    data_moved_count = 0
    
    def __init__(self, data):
        self.data=data
        self.n=len(self.data)-1

    def __str__(self):
        return str(self.data)
    
    def addElt(self,elt):
        self.n += 1
        self.data.append(elt)
        self.siftUp(self.n)
    
    def siftUp(self, i):
        child = i
        parent = math.floor(i/2)
        while(child>=2):
            if self.data[child] > self.data[parent]:
                self.data_moved_count += 1
                self.data[parent], self.data[child] = self.data[child], self.data[parent]
                child = parent
                parent = math.floor(child/2)
            else:
                break

    def siftDown(self,i):
        if i*2 > self.n : return
        parent = i
        large_child = 2*i
        if self.n >= 2*i+1 and self.data[2*i] < self.data[2*i+1]: 
            large_child = 2*i+1

        while(self.data[parent] < self.data[large_child]):
            self.data[parent], self.data[large_child] = self.data[large_child], self.data[parent]
            self.data_moved_count += 1
            parent = large_child

            if 2*parent > self.n : 
                break
            large_child = 2*parent
            if self.n >= 2*parent+1 and self.data[parent*2] < self.data[2*parent+1]:
                large_child = 2*parent+1

    def makeHeap1(self): 
        self.data_moved_count = 0
        old_data = self.data
        self.data = [0]
        for i in range(1,self.n+1):
            self.data.append(old_data[i])
            self.siftUp(i)

    def makeHeap2(self): 
        self.data_moved_count = 0
        d = math.floor(math.log2(self.n))
        for i in range(d,0,-1):
            for j in range(2**(i-1),2**i):
                self.siftDown(j)

    def root(self):
        keyout = self.data[1]
        self.data[1] = self.data[self.n]
        del self.data[self.n]
        self.n -= 1
        if(self.n>0):
            self.siftDown(1)
        return keyout
    
    def removeKeys(self):
        result = []
        for i in range(self.n):
            result.append(self.root())
        return result

def heapSort1(a):
    h = Heap(a)
    h.makeHeap1()
    c = h.data_moved_count
    return h.removeKeys(), c

def heapSort2(a):
    h = Heap(a)
    h.makeHeap2()
    c = h.data_moved_count
    return h.removeKeys(), c
        
a=[0,5,9,2,17,6,13,11,7,15]

print("===== 방법 1 =====")
print("결과 : {0}\n데이터 이동 횟수 : {1} 회\n".format(*heapSort1(a.copy())))

print("===== 방법 2 =====")
print("결과 : {0}\n데이터 이동 횟수 : {1} 회".format(*heapSort2(a.copy())))