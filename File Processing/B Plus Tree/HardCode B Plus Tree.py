import pickle
Maxkeys = 4
fixedsize = 200                 # Fixed size of each object in index file
class IndexNode:
    '''
    Objective : To create a node in index file.
    '''
    def __init__(self):
        '''
        Objective        : To initialize an object of class IndexNode
        Input Parameters :
            self(Implicit parameter)-> Object of type IndexNode
            Maxkeys                 -> Maximum number of keys in a node.
        Output           : None
        '''
        self.keys = [(9999,9999)]*Maxkeys
        self.pointers =[9999]*(Maxkeys + 1)
        self.currindex = 0
        self.linkindex = 0
        
    
    def __str__(self):
        '''
        Objective        : To return string representation of object.
        Input Parameters :
            self(Implicit parameter)-> Object of type IndexNode
        Output           : String
        '''
        return str(self.keys)+' || '+str(self.pointers)
        
def nodekey(nodetup):
    '''
    Objective        : To return key of a given tuple.
    Input Parameters :
             nodetup-> tuple
    Output           : First element(key ) of tuple.
    '''
    #if isinstance(nodetup,int):return nodetup
    return nodetup[0]

def InsertKey(node,key):
    '''
    Objective        : To insert a key in a given node.
    Input Parameters :
                node-> Object of IndexNode class
                key -> Number
               index-> Positive number
    Output           : None
    '''
    node.keys[node.currindex]=(key)
    node.currindex+=1
    node.keys.sort(key = nodekey)

def Split(node,rootnode,splitnode,nodelink=[],linkslist=[],key=(9999,9999),splitnodelink=[],doublesplit = False):
    tmp = node.keys + [key]
    tmp.sort(key=nodekey)
    node.currindex+=1
    node.currindex = node.currindex//2
    remaining = Maxkeys-node.currindex
    node.keys[:node.currindex]=tmp[:node.currindex]
    node.keys[node.currindex:Maxkeys]=[(9999,9999)]*(remaining)
    node.pointers[:len(nodelink)] = nodelink
    node.pointers[len(nodelink):] = [9999]*(Maxkeys+1-len(nodelink))

    if doublesplit :
        splitnode.keys[:remaining+1] = tmp[node.currindex+1:]
        splitnode.currindex += (remaining)
    else :
        splitnode.keys[:remaining+1] = tmp[node.currindex:]
        splitnode.currindex += (remaining +1)
    splitnode.keys.sort(key = nodekey)
    splitnode.pointers[:len(splitnodelink)]=splitnodelink
    

    rootnode.keys[rootnode.currindex]=tmp[node.currindex]
    rootnode.currindex +=1
    rootnode.keys.sort(key=nodekey)
    rootnode.pointers[:len(linkslist)]=linkslist
    rootnode.pointers[len(linkslist):]= [9999]*(Maxkeys+1-len(linkslist))
    
    
def PrintFile():
    '''
    Objective : To display index file
    '''
    print('\n***************Index File*******************\n')
    indexfile = open('IndexFile','rb')
    while True:
        try:
            print(pickle.load(indexfile))
        except EOFError: break
    
# Records
'''
40   10   60   5    9    86   29   12   55   36   44   24   8   4   90   34   74   22   26   28   50
'''

# node for location of root node
loc = IndexNode()
node1 = IndexNode()
node2 = IndexNode()
node3 = IndexNode()

loc.keys[0]=(1,9999)

indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
indexfile.close()
#PrintFile()

# Insert 40
InsertKey(node1,(40,0))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
indexfile.close()
#PrintFile()

# Insert 10
InsertKey(node1,(10,1))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
indexfile.close()
#PrintFile()

# Insert 60
InsertKey(node1,(60,2))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
indexfile.close()
#PrintFile()

# Insert 5
InsertKey(node1,(5,3))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
indexfile.close()
#PrintFile()

# Insert 9
Split(node1,node3,node2,[2],[1,2],(9,4))
loc.keys[0]=(3,9999)
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
indexfile.close()
#PrintFile()


# Insert 86
InsertKey(node2,(86,5))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
indexfile.close()
#PrintFile()

# Insert 29
node4= IndexNode()
Split(node2,node3,node4,[4],[1,2,4],(29,6))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
indexfile.close()
#PrintFile()

# Insert 12
InsertKey(node2,(12,7))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
indexfile.close()
#PrintFile()

# Insert 55
InsertKey(node4,(55,8))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
indexfile.close()
#PrintFile()

# Insert 36
InsertKey(node2,(36,9))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
indexfile.close()
#PrintFile()

# Insert 44
node5 = IndexNode()
Split(node4,node3,node5,[5],[1,2,4,5],(44,10))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
pickle.dump(node5,indexfile)
indexfile.close()
#PrintFile()

# Insert 24
node6 = IndexNode()
Split(node2,node3,node6,[6],[1,2,6,4,5],(24,11),[4])
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
pickle.dump(node5,indexfile)
pickle.dump(node6,indexfile)
indexfile.close()
#PrintFile()

# Insert 8
InsertKey(node1,(8,12))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
pickle.dump(node5,indexfile)
pickle.dump(node6,indexfile)
indexfile.close()
#PrintFile()

# Insert 4
InsertKey(node1,(4,13))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
pickle.dump(node5,indexfile)
pickle.dump(node6,indexfile)
indexfile.close()
#PrintFile()

# Insert 90
InsertKey(node5,(90,14))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
pickle.dump(node5,indexfile)
pickle.dump(node6,indexfile)
indexfile.close()
#PrintFile()

# Insert 34
InsertKey(node6,(34,15))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
pickle.dump(node5,indexfile)
pickle.dump(node6,indexfile)
indexfile.close()
#PrintFile()

# Insert 74
node7 = IndexNode()
node8 = IndexNode()
node9 = IndexNode()
loc.keys[0]=(9,9999)
Split(node5,node8,node7,[7],[4,5,7],(74,16))
Split(node3,node9,node8,[1,2,6],[3,8],(74,16),[4,5,7],True)
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
pickle.dump(node5,indexfile)
pickle.dump(node6,indexfile)
pickle.dump(node7,indexfile)
pickle.dump(node8,indexfile)
pickle.dump(node9,indexfile)
indexfile.close()
#PrintFile()

# Insert 22
node10 = IndexNode()
Split(node6,node3,node10,[10],[1,2,6,10],(22,17),[4])
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
pickle.dump(node5,indexfile)
pickle.dump(node6,indexfile)
pickle.dump(node7,indexfile)
pickle.dump(node8,indexfile)
pickle.dump(node9,indexfile)
pickle.dump(node10,indexfile)
indexfile.close()
#PrintFile()

# Insert 26
InsertKey(node6,(26,18))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
pickle.dump(node5,indexfile)
pickle.dump(node6,indexfile)
pickle.dump(node7,indexfile)
pickle.dump(node8,indexfile)
pickle.dump(node9,indexfile)
pickle.dump(node10,indexfile)
indexfile.close()
#PrintFile()

# Insert 28
InsertKey(node6,(28,19))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
pickle.dump(node5,indexfile)
pickle.dump(node6,indexfile)
pickle.dump(node7,indexfile)
pickle.dump(node8,indexfile)
pickle.dump(node9,indexfile)
pickle.dump(node10,indexfile)
indexfile.close()
#PrintFile()

# Insert 50
InsertKey(node4,(50,20))
indexfile = open('IndexFile','wb')
pickle.dump(loc,indexfile)
pickle.dump(node1,indexfile)
pickle.dump(node2,indexfile)
pickle.dump(node3,indexfile)
pickle.dump(node4,indexfile)
pickle.dump(node5,indexfile)
pickle.dump(node6,indexfile)
pickle.dump(node7,indexfile)
pickle.dump(node8,indexfile)
pickle.dump(node9,indexfile)
pickle.dump(node10,indexfile)
indexfile.close()
PrintFile()

size=[0]
f = open('IndexFile','rb')
while True:
    try:
        prev = f.tell()
        pickle.load(f)
        #print(f.tell())
        size.append(fixedsize-(f.tell()-prev))
        #print(size)
    except EOFError:break
f.close()
size[0] = fixedsize
#print(*size)

def SearchIntermediate(key,searchnode,file):
    '''
    Objective        : To recursively search a key in b plus Tree
    Input Parameters :
            key        -> Key to be searched
            searchnode -> Node index in which key is to be searched
            file       -> File in which nodes are stored
    Output           : 1 if key is present ;otherwise 0
    '''
    if searchnode == 9999:print(key,' Not Present!!')
    else:
        pos = ((searchnode+1)* fixedsize)- sum(size[:searchnode+1])
        file.seek(pos)
        node = pickle.load(file)
        if key in [ele[0] for ele in node.keys]:print(key,' Found')
        else:
            maxkey = [ele for ele in  node.keys if ele[0]>key]
            if maxkey == []:newsearchnode = node.pointers[-1]
            else:
                tmp = node.keys.index(maxkey[0])
                newsearchnode = node.pointers[tmp]
            #print('maxkey',tmp)
            #print('pointer',newsearchnode)
            SearchIntermediate(key,newsearchnode,file)
    
def Search(key):
    '''
    Objective        : To search a particular key in b plus tree
    Input Parameters :
                key -> Number to be searched
    Output           : None
    '''
    # Approach : Make use of SearchIntermediate Function.
    f = open('IndexFile','rb')
    rootnode = pickle.load(f)
    searchnode = rootnode.keys[0][0]
    SearchIntermediate(key,searchnode,f)
    f.close()
    
if __name__ == '__main__':
    ch = 'Y'
    while ch == 'Y' or ch == 'y':
        KEY = int(input('Enter key to be searched : '))
        Search(KEY)
        ch = input('Do you want to continue ?(Y or y for Yes) : ')
        

    



