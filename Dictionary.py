class DictPair:
    '''
    Objective : To create a key-value pair of dictionary.
    '''
    def __init__(self,key,value):
        '''
        Objective        : To initialize an object of class DictPair.
        Input Parameters :
        self(Implicit Parameter) -> Object of class DictPair.
                             key -> key
                           value -> value
        Output           : None
        '''
        self.key = key
        self.value = value

    def __str__(self):
        '''
        Objective        : To return string representation of class DictPair.
        Input Parameters :
        self(Implicit Parameter) -> Object of class DictPair.
        Output           : String
        '''
        return self.key+' : '+self.value
        

class Dictionary:
    '''
    Objective : To implement a dictionary using a list.
    '''
    def __init__(self):
        '''
        Objective        : To initialize an object of class Dictionary.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Dictionary.
        Output           : None
        '''
        self.dict = []

    def Keys(self):
        '''
        Objective : To determine all keys in a dictionary.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Dictionary.
        Output           : list
        '''
        keys = []
        if self.dict == []: return []
        for pair in self.dict:
            keys.append(pair.key)
        return keys

    def Values(self):
        '''
        Objective : To determine all values in a dictionary.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Dictionary.
        Output           : list
        '''
        values = []
        if self.dict == []: return []
        for pair in self.dict:
            values.append(pair.value)
        return values

    def Items(self):
        items = []
        if self.dict == []: return []
        for pair in self.dict:
            items.append(pair)
        return items
        

    def Insert(self,obj):
        '''
        Objective         : To insert an object of class DictPair in dictionary.
         Input Parameters :
        self(Implicit Parameter) -> Object of class DictPair.
                             obj -> Object of class Dictionary that consists of key and value.
        Output           : None
        '''
        if self.dict == [] : self.dict.append(obj)
        elif obj.key in self.Keys() :
            ind = self.Keys().index(obj.key)
            self.dict[ind].value = obj.value
        else : self.dict.append(obj)
        
        
    def get(self , key):
        '''
        Objective         : To return value corresponding to a key.
         Input Parameters :
        self(Implicit Parameter) -> Object of class DictPair.
                             key -> key of Dictionary whose value is to be returned.
        Output           : None
        '''
        if key not in self.Keys() : return '\nKEY DOES NOT EXIST!!'
        for pair in self.dict:
            if pair.key == key:
                return pair.value
        

    def set(self , key , val):
        '''
        Objective         : To update value corresponding to a key.
         Input Parameters :
        self(Implicit Parameter) -> Object of class DictPair.
                             key -> key of Dictionary whose value is to be updated.
                             val -> New value
        Output           : None
        '''
        if key not in self.Keys() : return '\nKEY DOES NOT EXIST!!'
        for pair in self.dict:
            if pair.key == key:
                pair.value = val
                break

    
    def Delete(self , key):
        '''
        Objective         : To delete a key-value pair.
         Input Parameters :
        self(Implicit Parameter) -> Object of class DictPair.
                             key -> key of key-value pair to be deleted.
        Output           : None
        '''
        if self.dict == []:
            print('\nDictionary is empty !!')
            return
        try:
            ind = self.Keys().index(key)
            self.dict.pop(ind)
            print('\nKey - Value pair successfully deleted.')
        except:
            print('\nKey - Value pair does not exist!')
        
    def __str__(self):
        '''
        Objective        : To return string representation of class Dictionary.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Dictionary.
        Output           : String
        '''
        if self.dict == []:
            return '\nDictionary is empty !!'
        l = []
        for pair in self.dict:
            l.append(pair)
        return '{'+' , '.join(str(x) for x in l)+'}'

if __name__ == '__main__':
    print('***********************DICTIONARY OPERATIONS***********************')
    d = Dictionary()
    ch = 'y'
    while ch in ['y' , 'Y']:
        print('\nFollowing Operations can be performed :')
        print('\n1. Insert a pair \n2. Delete a pair  \n3. Get the value of a key  \n4. Update a key  \n5. Print Dictionary \n6. Print all keys in dictionary \n7.Print all values in dictionary \n8. Print all pairs in dictionary ')   
        choice = int(input('\nEnter your choice : '))
        if choice == 1 :
            key = input('\nEnter key : ')
            val = input('\nEnter value : ')
            d.Insert(DictPair(key,val))
        elif choice == 2 :
            key = input('\nEnter key : ')
            d.Delete(key)   
        elif choice == 3 :
            key = input('\nEnter key : ')
            print(d.get(key))
        elif choice == 4 :
            key = input('\nEnter key to be updated : ')
            val = input('\nEnter new value : ')
            d.set(key,val)
        elif choice == 5 :
            print('\nDICTIONARY : ','\n',d)
        elif choice == 6 :
            print('\nKEYS :')
            print(d.Keys())
        elif choice == 7 :
            print('\nVALUES :')
            print(d.Values())
        elif choice == 8 :
            print('\nKEY - VALUE PAIRS :')
            print(d.Items())
        else:
            break
        ch = input('\nDo you want to continue(y or Y for yes) ? ')
            
    '''        
    d.Insert(DictPair('a',65))
    d.Insert(DictPair('b',66))
    d.Insert(DictPair('c',67))
    d.Insert(DictPair('d',68))
    d.Insert(DictPair('a',78))
    print(d)
    d.set('d',98)
    print(d)
    d.Delete('c')
    print(d)
    '''
    
    
        
        
