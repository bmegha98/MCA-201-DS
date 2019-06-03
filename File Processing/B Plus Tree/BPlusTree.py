import pickle,DataFile,IndexFile
nil = 9999

class BplusTree:
    '''
    Objective  : To create a Bplus Tree.
    '''
    def __init__(self,Maxkeys):
        '''
        Objective        : To create b plus tree data structure.
        Input Parameters :
         self(Implicit parameter)-> Object of type BplusTree
        Output           : None
        '''
        self.Maxkeys = Maxkeys
        self.nodelist = []
        self.rootinfo = IndexFile.IndexNode(Maxkeys)
        self.rootinfo.keys[0] = (1,nil)
        self.nodelist.append(self.rootinfo)
        
        root = IndexFile.IndexNode(Maxkeys)
        self.nodelist.append(root)

    def FindNodeToInsert(self, key ):
        '''
        Objective        : To find a node in which given key is to be inserted.
        Input Parameters :
          self(Implicit parameter)-> Object of type BplusTree
                               key-> Key to be added.
        Output           : Node in which key to be inserted.
        '''
        rootindex = self.rootinfo.keys[0][0]
        currnode = self.nodelist[rootindex] 
       
        while not currnode.isleaf:
            i = 0
            while True:
                if i == self.Maxkeys or currnode.keys[i][0]== nil or currnode.keys[i][0]>key:break
                i+=1
            
            currnode = self.nodelist[currnode.pointers[i]]
            
        
        return currnode

    def Parent(self,currnode):
        '''
        Objective        : to find parent node of currnode.
        Input Parameters :
            self(Implicit parameter)-> Object of type BplusTree
                           currnode -> Node of B+ Tree whose parent node is to be determined.
        Output           : Node of B+ Tree.
        '''
        nodeindex = self.nodelist.index(currnode)
        Parentnode = IndexFile.IndexNode(self.Maxkeys)
        for node in self.nodelist:
            if (not node.isleaf) and (nodeindex  in node.pointers):
                Parentnode = node
                break
        return Parentnode

    def Insert(self,keytup):
        '''
        Objective        : To insert a key in desired node.
        Input parameters :
        self(Implicit parameter)-> Object of type BplusTree
                             key-> Key tuple to be added.
        Output           : None
        '''
        current = self.FindNodeToInsert(keytup[0])
        
        try:
            current.add(keytup)
        except:
            self.balance(current,keytup)
        self.makeIndexFile()
        self.makeIndexPosFile()

    def balance(self,splitnode,key=None):
        '''
        Objective        : To balance b plus tree in case current node is full.
        Input Parameters :
        self(Implicit parameter)-> Object of type BplusTree
                           node -> Current node in which key-value tuple to be added.
                            key -> Key to be inserted.
        Output           :  None     
        '''
        midtup , newnode = splitnode.split(key)
       
        parent = self.Parent(splitnode)
        self.nodelist.append(newnode)
        parent.keys = parent.keys[:parent.currindex]+([midtup])+[(nil,nil)]*(self.Maxkeys - parent.currindex-1)
        parent.keys.sort(key = nodekey)
        parent.currindex+=1
        
        
        if (self.nodelist.index(splitnode)) not in parent.pointers:
            parent.isleaf = False
            self.nodelist.append(parent)
            # Updating root 
            self.rootinfo.keys[0] = (len(self.nodelist)-1 , nil)
            
            parent.pointers[parent.linkindex] = self.nodelist.index(splitnode)
            parent.linkindex +=1

        keysTemp = [nodekey(x) for x in parent.keys]
        i = keysTemp.index(nodekey(midtup)) 
        parent.pointers = parent.pointers[:i+1]+[self.nodelist.index(newnode)]+parent.pointers[i+1:parent.linkindex]+[nil]*(self.Maxkeys-parent.linkindex)
        parent.linkindex +=1
        
        # Linking between leaf nodes
        if splitnode.isleaf:
            if splitnode.currindex!=0:
                newnode.pointers[0] = splitnode.pointers[0]
            splitnode.pointers[0]= self.nodelist.index(newnode)
        else:
            mid = self.Maxkeys // 2
            newnode.pointers = splitnode.pointers[mid+1:self.Maxkeys+2]+[nil]*(self.Maxkeys-mid)
            splitnode.pointers = splitnode.pointers[:mid+1]+[nil]*(self.Maxkeys-mid)
            splitnode.linkindex = (mid+1)
            newnode.linkindex =(self.Maxkeys+2- splitnode.linkindex)
    
        if len(parent.keys) > self.Maxkeys and len(parent.pointers) > (self.Maxkeys+1) : self.balance(parent)
        
    def SearchKey(self,key):
        '''
        Objective        : To search a key in B+ tree.
        Input Parameters :
            self(Implicit parameter)-> Object of type BplusTree
                                key -> Key to be searched
        Output           : Key-value pair if key exists;otherwise None.
        '''
        file = open('indexfile.bin','rb')
        rootindex = pickle.load(file).keys[0][0]
        currnode = self.getNodeFromIndexFile(rootindex)
        while not currnode.isleaf:
            i = 0
            while True:
                if i == self.Maxkeys or currnode.keys[i][0] == nil or currnode.keys[i][0] > key: break
                i += 1
            currnode = self.getNodeFromIndexFile(currnode.pointers[i])
        currentKeys = [nodekey(x) for x in currnode.keys]
        if key in currentKeys:
            return currnode , currnode.keys[currentKeys.index(key)]
        else:
            return None
        file.close()

    def SearchUtil(self,key,currindex,i=0):
        '''
        Objective        : To search a key recursively in B+ tree.
        Input Parameters :
            self(Implicit parameter)-> Object of type BplusTree
                                key -> Key to be searched
                               file -> File pointer
                          currindex -> Index of current node
        Output           : Key-value pair if key exists;otherwise None.
        '''
        currnode = self.getNodeFromIndexFile(currindex)
        if currnode.isleaf == True : return currnode
        
        if i == Maxkeys or currnode.keys[i][0] == nil or currnode.keys[i][0] > key :
            return self.SearchUtil(key,currnode.pointers[i],0)
        return self.SearchUtil(key,currindex,i+1)
        
        
        

    def SearchKeyRec(self,key):
        '''
        Objective        : To search a key in B+ tree.
        Input Parameters :
            self(Implicit parameter)-> Object of type BplusTree
                                key -> Key to be searched
        Output           : Key-value pair if key exists;otherwise None.
        '''
        file = open('indexfile.bin','rb')
        rootindex = pickle.load(file).keys[0][0]
        res = self.SearchUtil(key,rootindex)
        currkeys = [nodekey(x) for x in res.keys]
        if key in currkeys :
            return res,res.keys[currkeys.index(key)]
        return None
        file.close()
        
        
           
    def PrintKeysInRange(self , key , n):
        '''
        Objective        : To search a key in B+ tree.
        Input Parameters :
            self(Implicit parameter)-> Object of type BplusTree
                                key -> key to be searched
                                  n -> Number of keys to be printed after finding desired key.
        Output           : None
        '''
        res = self.SearchKey(key)
        currnode = res[0]
        keyindex = currnode.keys.index(res[1])
        count = 0
        i = keyindex
        while True:
            while True:
                if count == n or i == self.Maxkeys or currnode.keys[i][0] == nil : break
                print(currnode.keys[i][0],'\n')
                i+=1
                count+=1
                
            if count == n or currnode.pointers[0] == nil:break
            currnode = self.getNodeFromIndexFile(currnode.pointers[0])
            i = 0
        
        
    def makeIndexFile(self):
        '''
        Objective        : To create index file of B plus Tree.
        Input Parameters :
            self(Implicit parameter)-> Object of type BplusTree
        Output           : None
        '''
        
        file = open('indexfile.bin','wb')
        for n in self.nodelist:
            pickle.dump(n,file)
        file.close()

    def makeIndexPosFile(self):
        '''
        Objective        : To create an index position file a B+ tree.
        Input Parameters :
            self(Implicit parameter)-> Object of type BplusTree
        Output           : None
        '''
        indexposlist =[]
        indexfile = open('indexfile.bin','rb')
        while True:
            indexposlist.append(indexfile.tell())
            try:
                pickle.load(indexfile)
            except EOFError:
                break
        indexposfile = open('indexposfile.bin','wb')
        pickle.dump(indexposlist,indexposfile)
        indexfile.close(),indexposfile.close()
        
    def getNodeFromIndexFile(self,nodeindex):
        '''
        Objective        : To retrieve the node from given location.
        Input Parameters :
            self(Implicit parameter)-> Object of type BplusTree
                          nodeindex -> Index of node to be retrieved.
        Ouput            : Object of IndexNode class.
        '''
        f1 = open('indexposfile.bin','rb')
        poslist = pickle.load(f1)
        f2 = open('indexfile.bin','rb')
        f2.seek(poslist[nodeindex])
        return pickle.load(f2)

    
    def PrintIndexFile(self):
        '''
        Objective        : To print index file of B plus Tree.
        Input Parameters :
            self(Implicit parameter)-> Object of type BplusTree
        Output           : None
        '''
        print('\n**********************Index File*******************\n')
        file = open('indexfile.bin','rb')
        while True:
            try:
                print(pickle.load(file))
            except EOFError : break
        file.close()

def nodekey(nodetup):
    '''
    Objective        : To return key of a given tuple.
    Input Parameters :
             nodetup-> tuple
    Output           : First element(key ) of tuple.
    '''
    
    return nodetup[0]

def CreateBPlusTree(filename,Maxkeys):
    '''
    Objective        : To create a B+ Tree of records.
    Input Parameters :
            filename -> Name of file whose records are used to create B+ Tree.
                   b -> Object of BpluTree
    Output           :  None
    '''
    file = open(filename,'rb')
    b = BplusTree(Maxkeys)
    i = 0
    while True:
        try :
            record = pickle.load(file)
            key = DataFile.RecordKey(record)
            b.Insert((key,i))
            i+=1
        except EOFError :
            break
    file.close()
    return b
        

def HardCodeTree(Maxkeys):
    '''
    Objective : To create a B+ Tree with keys entered manually.
    '''
    
    b = BplusTree(Maxkeys)
    # Insert 40
    b.Insert((40,0))

    # Insert 10
    b.Insert((10,1))

    # Insert 60
    b.Insert((60,2))

    # Insert 5
    b.Insert((5,3))

    # Insert 9
    b.Insert((9,4))

    # Insert 86
    b.Insert((86,5))

    # Insert 29
    b.Insert((29,6))

    # Insert 12
    b.Insert((12,7))

    # Insert 55
    b.Insert((55,8))

    # Insert 36
    b.Insert((36,9))

    # Insert 44
    b.Insert((44,10))

    # Insert 24
    b.Insert((24,11))

    # Insert 8
    b.Insert((8,12))

    # Insert 4
    b.Insert((4,13))

    # Insert 90
    b.Insert((90,14))

    # Insert 34
    b.Insert((34,15))
    
    # Insert 74
    b.Insert((74,16))
   
    # Insert 22
    b.Insert((22,17))
    
    # Insert 26
    b.Insert((26,18))
    
    # Insert 28
    b.Insert((28,19))
    
    # Insert 50
    b.Insert((50,20))
    
    # Insert 92
    b.Insert((92,21))
    
    # Insert 88
    b.Insert((88,22))
    
    # Insert 96
    b.Insert((96,23))
    
    # Insert 98
    b.Insert((98,24))
  
    # Insert 99
    b.Insert((99,25))
    
    # Insert 105
    b.Insert((105,26))
    return b
    

if __name__=='__main__':
    '''
    Maxkeys = int(input('Enter max number of keys : '))
    t = HardCodeTree(Maxkeys)
    t.PrintIndexFile()
    ans = t.SearchKeyRec(88)
    if ans:
        print(ans[0],ans[1])
    else: print('NONE')
    '''
    
    NumberOfRecords = int(input('Enter number of records : '))
    Maxkeys = int(input('Enter max number of keys : '))
    DataFile.createDataFile(NumberOfRecords)
    
    t = CreateBPlusTree('dataFile.bin',Maxkeys)
    t.PrintIndexFile()
    
    while True:
        try:
            key = int(input('\nEnter key to be searched : '))
            n = int(input('\nEnter number of keys to be fetched :  '))
        except:
            print('The value of key must be a positive number !!')

        keytup = t.SearchKeyRec(key)
        if keytup:
            keytup = keytup[1]
            print('FOUND !!! The given key exists as -> ',keytup)
            print('\n Record from data file with  key',key,': ',DataFile.fetchRecord('dataFile.bin',keytup[1]))
        else:
            print('NOT FOUND !!! The given key does not exists.')

        if keytup :
            print(n,' Keys after',key ,' are :\n')
            t.PrintKeysInRange(key,n)

        c = None
        while c not in ['y' ,'Y' ,'n' ,'N']:
            c = input('\n Do you want to continue(y/n) ??')
        if c == 'n' or c == 'N':break
    
          
            
                  
                  
                  
       
            
        
    
            
            
        
        
        
        



