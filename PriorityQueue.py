import math
class PQueue:
    '''
    Objective : To implement priority queue .
    '''
    def __init__(self):
        '''
        Objective        :  To initialize an object of class PQueue .
        Input Parameters :
                    self -> Implicit object of class PQueue.
        Output           :  None
        '''
        self.queue = []

    def Enqueue(self , ele):
        '''
        Objective        :  To insert an element in priority queue .
        Input Parameters :
                    self -> Implicit object of class PQueue.
                     ele -> Number
        Output           :  None
        '''
        if self.queue == []: self.queue.append(ele)
        else:
            self.queue.append(ele)
            i = len(self.queue)-1
            while i>0:
                parent = math.floor((i-1)/2)
                if self.queue[parent]< ele:
                    self.queue[i] = self.queue[parent]
                    i = parent
                else :
                    break           
            self.queue[i] = ele

    def Dequeue(self):
        '''
        Objective        :  To delete highest priority element i.e. root of maxheap from the priority queue .
        Input Parameters :
                    self -> Implicit object of class PQueue.
        Output           :  None
        '''
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        root = self.queue[0]
        i = 0
        while i<len(self.queue):
            left , right = (2*i+1) , (2*i+2)
            if left >= len(self.queue) : break
            if left < len(self.queue) and right >= len(self.queue): maxchild = self.queue[left]
            else:
                maxchild = max(self.queue[left],self.queue[right])
            
            if maxchild > root:
                self.queue[i] = maxchild
                i = left if maxchild is self.queue[left] else right
            else:
                break
        self.queue[i] = root
        

    def __str__(self):
        '''
        Objective        :  To return string representation of object of PQueue .
        Input Parameters :
                    self -> Implicit object of class PQueue.
        Output           :  String
        '''
        return ' '.join(str(x) for x in self.queue)

if __name__ == '__main__':
    p = PQueue()
    p.Enqueue(16)
    p.Enqueue(40)
    p.Enqueue(7)
    p.Enqueue(23)
    p.Enqueue(18)
    p.Enqueue(12)
    print(p)
    p.Dequeue() 
    print(p)
    
                
        
