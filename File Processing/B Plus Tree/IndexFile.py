
nil = 9999

class IndexNode:
    '''
    Objective : To create a node in index file.
    '''
    def __init__(self,Maxkeys,isleaf=True):
        '''
        Objective        : To initialize an object of class IndexNode
        Input Parameters :
            self(Implicit parameter)-> Object of type IndexNode
            Maxkeys                 -> Maximum number of keys in a node.
        Output           : None
        '''
        self.keys = [(nil,nil)]*Maxkeys
        self.pointers =[nil]*(Maxkeys + 1)
        self.Maxkeys = Maxkeys
        self.currindex = 0
        self.linkindex = 0
        self.parent = None
        self.isleaf = isleaf
      
        
    
    def __str__(self):
        '''
        Objective        : To return string representation of object.
        Input Parameters :
            self(Implicit parameter)-> Object of type IndexNode
        Output           : String
        '''
        return str(self.keys)+' || '+str(self.pointers)

    def add(self,keytup):
        '''
        Objective        : To add a key tuple in node.
        Input Parameters :
         self(Implicit parameter)-> Object of type IndexNode
                          keytup -> key-record_number tuple
        Output           : None
        '''
        self.keys[self.currindex]=keytup
        self.currindex+=1
        self.keys.sort(key = nodekey)

    def split(self,keytup=None):
        '''
        Objective        : To split a node and return newly created node.
        Input Parameters :
         self(Implicit parameter)-> Object of type IndexNode
                          keytup -> key-record_number tuple
        Output           : Middle element or None and newly created node.  
        '''
        temp = self.keys + ([keytup] if keytup else [])
        temp.sort(key = nodekey)
        mid = self.currindex//2
        
        self.keys = temp[:mid] + [(nil,nil)]*(self.Maxkeys-mid)
        self.currindex = mid
        isLeaf = self.isleaf
        newNode = IndexNode(self.Maxkeys,isLeaf)
        newNode.keys = (temp[mid:] if isLeaf else temp[mid+1:]) + [(nil,nil)]*((self.Maxkeys-mid-1) if keytup else (self.Maxkeys-mid))
        newNode.currindex = self.Maxkeys-mid+1 if keytup else (self.Maxkeys-mid)
        return temp[mid], newNode

def nodekey(nodetup):
    '''
    Objective        : To return key of a given tuple.
    Input Parameters :
             nodetup-> tuple
    Output           : First element(key ) of tuple.
    '''
    
    return nodetup[0]

