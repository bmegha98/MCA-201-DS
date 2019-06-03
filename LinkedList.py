class Node:
    def __init__(self,value):
        '''
        Objective          : To create a node.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
                           value-> value of node.
        Output             : Node with data part equal to value and a link to the next node.
        '''
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        '''
        Objective          : To initialize the head pointer.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
        Output             : None
        '''
        self.head=None

    def InsertAtBeginning(self,value):
        '''
        Objective          : To insert a node at the beginning of a linked list.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
                           value-> value of node to be inserted.
        Output             : None
        '''
        node=Node(value)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def InsertAtEnd(self,value):
        '''
        Objective          : To insert a node at the end of a linked list.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
                           value-> value of node to be inserted.
        Output             : None
        '''
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            r = self.head
            while r.next!=None:
                r = r.next
            r.next = node
                    
    def InsertSorted(self,value):
        '''
        Objective          : To insert a node in sorted list.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
                           value-> value of node to be inserted.
        Output             : None
        '''

        node = Node(value)
        if self.head == None : self.head = node
        else:
            r ,prev = self.head,None
            while r!=None:
                if r.data <= value:
                    prev = r
                    r = r.next
                else:
                    break
            if prev : prev.next = node
            if r == self.head : self.head = node
            node.next = r
            
    def ReverseList(self):
        '''
        Objective          : To reverse the linked list.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
        Output             : None
        '''
        prev = None
        curr = self.head
        while curr!=None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        self.head = prev

    def ReverseListRec(self,prev = None , curr = -1):
        '''
        Objective          : To reverse the linked list recursively.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
        Output             : None
        '''
        if self.head == None: return
        if curr == None:
            self.head = prev
            return
        if curr == -1:curr = self.head
        tmp = curr.next
        curr.next = prev
        self.ReverseListRec(curr,tmp)
        

    def MiddleElement(self):
        '''
        Objective          : To determine middle element of the linked list.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
        Output             : Node
        '''
        if self.head == None: return '\nList is empty!'
        fast = self.head
        slow = self.head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def Present(self , ele):
        r = self.head
        while r!=None:
            if r.data == ele:
                return True
            r = r.next
        return False
             
    def Intersection(self,List):
        '''
        Objective          : To determine intersection of two sorted linked lists.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
                           List -> Sorted Linked List
        Output             : Linked List
        '''
        intersection = LinkedList()
        r = self.head
        while r!=None:
            if List.Present(r.data):
                intersection.InsertAtEnd(r.data)
            r = r.next
        return intersection
        
        
    def DeleteNode(self,value):
        '''
        Objective          : To delete a node with data part equal to value.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
                           value-> value of node to be deleted.
        Output             : Node if it is in the linked list otherwise None.
        '''
        p=self.head
        if p==None:
            print('Error !! List is Empty.')
            return  
        if p.data==value:
            self.head=p.next
            return p.data

        while p!=None:
            if p.data==value:
                r=self.head
                while r.next!=p:
                    r=r.next
                r.next=p.next
                return p.data
            else:
                p=p.next
        
        return None
                   
    def reverDisplay(self , node = -1):
        '''
        Objective          : To display linked list in reverse order.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
        Output             : None
        '''
        if self.head == None : return
        if node == -1 : node = self.head
        if node.next!=None:
            self.reverDisplay(node.next)
        print(node.data, end='  ')
        
    def __iadd__(self,val):
        '''
        Objective          : To increment value of each node in linked list by 1.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
        Output             : None
        '''
        r = self.head
        while r != None:
            r.data+=val
            r = r.next
        return self
        
    def __str__(self):
        '''
        Objective          : To return string representation of linked list.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
        Output             : String
        '''
        l=[]
        p=self.head
        if p==None:
            return "List is Empty."
        while p!=None:
            l.append(p.data)
            p=p.next

        return ' --> '.join(str(x) for x in l)

if __name__=='__main__':
    '''
    l1 , l2 ,l = LinkedList(), LinkedList() , LinkedList()
    l1.InsertAtEnd(1)
    l1.InsertAtEnd(4)
    l1.InsertAtEnd(7)
    l1.InsertAtEnd(10)
    print(l1)
    l1.ReverseListRec()
    print(l1)
   
    l2.InsertAtEnd(2)
    l2.InsertAtEnd(4)
    l2.InsertAtEnd(6)
    l2.InsertAtEnd(8)
    l2.InsertAtEnd(10)
    print(l2)
    print(l1.Intersection(l2))
    l1.reverDisplay()
    '''
    lsort = LinkedList()
    lsort.InsertSorted(22)
    lsort.InsertSorted(12)
    lsort.InsertSorted(20)
    lsort.InsertSorted(67)
    print(lsort)
    lsort+=1
    print(lsort)
  
    
    
    '''
    print('*************************************************LINKED LIST*****************************************')
    print('1. Create and Insert a node at beginning  \n2. Delete a node \n3. Display linked list \n4. Reverse Linked list  \n5. Middle Element of list \n6. Intersection of two sorted lists')
    l=LinkedList()
    while True:
        ch=int(input('\nEnter the choice 1/2/3/4 :  '))
        if ch == 1:
            node=int(input('Enter node to be inserted :'))
            l.InsertAtBeginning(node)

        elif ch == 2:
            node=int(input('Enter node to be deleted :'))
            print(l.DeleteNode(node))
        
        elif ch == 3:
            print('\nLINKED LIST :')
            print(l)

        elif ch == 4:
            print('\nREVERSE LINKED LIST :')
            l.ReverseList()
            print(l)
        elif ch == 5:
            print('\nMIDDLE ELEMENT OF LIST IS :')
            print(l.MiddleElement())
        else :
            print('!!!! WRONG CHOICE !!!!!')
        ch = input('\nDo you want to continue(y/n)?  ')
        if ch not in ['y','Y']:
            break
    '''

        

    



        
        
        
    
