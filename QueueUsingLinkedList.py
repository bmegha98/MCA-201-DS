class Node:
    '''
    Objective : To create a node of a linked list.
    '''
    def __init__(self , value):
        '''
        Objective        : To initialize an object of class Node.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Node
                           value -> Value of node
        Output           : None
        '''
        self.data = value
        self.next = None

        
class Queue:
    '''
    Objective : Implementation of queue using a linked list.
    '''
    def __init__(self):
        '''
        Objective        : To initialize an object of class Queue.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Queue
        Output           : None
        '''
        self.head = None
        self.last = None

    def Enqueue(self , ele):
        '''
        Objective        : To insert an element in queue.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Queue
                             ele -> Element to be inserted.
        Output           : None
        '''
        temp = Node(ele)
        if self.head == None and self.last == None:
            self.head = self.last = temp
        else:
            self.last.next = temp
            self.last = temp

    def Dequeue(self):
        '''
        Objective        : To delete an element from queue.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Queue
        Output           : None
        '''
        if self.head == None : return None
        print('\n',self.head.data,'Successfully deleted.')
        temp = self.head
        self.head = temp.next
        
        
    def __str__(self):
        '''
        Objective        : To return string representation of an object of class Queue.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Queue
        Output           : String
        '''
        queue = []
        p = self.head
        if p == None:
            return 'QUEUE IS EMPTY !!'
        print('\nQUEUE :')
        while p!=None:
            queue.append(p.data)
            p = p.next
        return ' || '.join(str(x) for x in queue)

if __name__ == '__main__':
    q = Queue()
    q.Enqueue(5)
    q.Enqueue(56)
    q.Enqueue(67)
    print(q)
    q.Dequeue()
    print(q)
    
        
        
