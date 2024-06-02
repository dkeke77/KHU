import math

class Heap(object):
    n=0
    
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
            parent = large_child

            if 2*parent > self.n : break
            large_child = 2*parent
            if self.n >= 2*parent+1 and self.data[parent*2] < self.data[2*parent+1]: 
                large_child = 2*parent+1

    def makeHeap2(self): 
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

def heapSort(a):
    H = Heap(a)
    H.makeHeap2()
    return H.removeKeys()
        
a=[0,11,14,2,7,6,3,9,5]
b=Heap(a)
b.makeHeap2()
print(b.data)
b.addElt(50)
print(b.data)
s=heapSort(a)
print(s)