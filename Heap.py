""" Implementation of a binary heap for numerical types
"""

from math import ceil

class Heap:

    def __init__(self,elemKey):
        self.arr=[]
        self.length=0
        self.elemKey=elemKey
    
    def add(self, element):
        self.arr.append(element)
        self.length+=1
        current=self.length-1
        parent=int(ceil(current/2.0))-1
        while self.arr[current][self.elemKey] < self.arr[parent][self.elemKey] and parent >= 0:
            self.arr[current],self.arr[parent]=self.arr[parent],self.arr[current]
            current=parent
            parent=int(ceil(current/2.0))-1
            
    def removeMin(self):
        if self.length==0:
            print "nothing to pop"
            return None
        retVal=self.arr[0]
        self.arr=[self.arr[-1]]+self.arr[1:-1]
        self.length-=1
        if self.length==0 or self.length==1:
            return retVal
        current=0
        min_child=None
        if self.length-1<2:
            min_child=1
        elif self.arr[1][self.elemKey]<self.arr[2][self.elemKey]:
            min_child=1
        else:
            min_child=2
        while self.arr[current][self.elemKey]>self.arr[min_child][self.elemKey]:
            self.arr[current],self.arr[min_child]=self.arr[min_child],self.arr[current]
            current=min_child
            if 2*current+2>self.length-1:
                if 2*current+1>self.length-1:
                    return retVal
                min_child=2*current+1
            elif self.arr[2*current+1]<self.arr[2*current+2]:
                min_child=2*current+1
            else:
                min_child=2*current+2
        return retVal
        
    def getSelf(self):
        print self.arr, len(self.arr), self.length
