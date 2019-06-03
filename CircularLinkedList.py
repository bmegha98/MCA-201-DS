class Node:
    def __init__(self,value):
        '''
        Objective          : To initialize an object of class Node.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
                           value-> value of node.
        Output             : None
        '''
        self.data = value
        self.next = None

class CLinkedList:
    '''
    Objective  :  To create a circular linked list.
    '''
    def __init__(self):
        '''
        Objective          : To initialize an object of class CLinkedList.
        Input parameters   :
        self(Implicit parameter)-> object of class CLinkedList
                           val  -> value of node.
        Output             : None
        '''
        self.head = None

    def Insert(self , val):
        '''
        Objective          : To insert a node at the end of a linked list.
        Input parameters   :
        self(Implicit parameter)-> Object of type CLinkedList.
                           value-> value of node to be inserted.
        Output             : None
        '''
        node = Node(val)
        
        if self.head == None :
            self.head = node
        else :
            r = self.head
            while r.next!=self.head:
                r = r.next
            r.next = node

        node.next = self.head
         

    def __str__(self):
        '''
        Objective          : To return string representation of linked list.
        Input parameters   :
        self(Implicit parameter)-> Object of type CLinkedList.
        Output             : String
        '''
        l=[]
        p=self.head
        if self.head == None:
            return "List is Empty."
        while p.next!=self.head:
            l.append(p.data)
            p=p.next

        l.append(p.data)

        return ' --> '.join(str(x) for x in l)

if __name__ == '__main__':

     l = CLinkedList()
     l.Insert(8)
     l.Insert(67)
     l.Insert(78)
     print(l)
            
            
        
