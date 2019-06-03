import pickle,random
import CreateIntermediateFiles,MergeFiles
class Record:
    '''
    Objective : To create a Record.
    '''
    def __init__(self, key, others):
        '''
        Objective        : To initialize an object of type Record.
        Input Parameters :
        self(Implicit Parameter)-> Object of type Record.
                             key-> Integer to represent key of record.
                          others-> String representing  information in record.
        Output           : None
        '''
        self.key=key
        self.others=others
    def __str__(self):
        '''
        Objective        : To return string representation of an object of type Record.
        Input Parameters :
        self(Implicit Parameter)-> Object of type Record
        Output           : String representation of given object.
        '''
        return 'KEY : ' + str(self.key)+'\tNON-KEY : ' + str(self.others)


def RecordSave(filename):
    '''
    Objective        : To save records in a file.
    Input Parameters :
            filename -> Name of file in which records are to be stored.
    Output           : None
    '''
    minrange,maxrange=2000000,8000000
    NOR,constant=100,5
    f=open(filename,'wb')
    for i in range(NOR):
        key=random.randrange(minrange,maxrange)
        others=str(key)*constant
        rec=Record(key,others)
        pickle.dump(rec,f)
        
    f.close()

def RangeRecords(Filename,StartRec,EndRec):
    '''
    Objective       : To retrieve records in range StartRec to EndRec.
    Input Parameters:
            Filename-> Name of file from which records are to be retrieved.
            StartRec-> Starting Record Number.
            EndRec  -> Ending Record Number.
    Output          :  None
    '''
    try:
        f=open(Filename,'rb')
        p=pickle.load(f)
        size=f.tell()
        start=f.seek(size*(StartRec-1))
        end=f.seek(size*(EndRec-1))
        f.seek(start)
        while start<=end:
            print(pickle.load(f))
            start+=size
        f.close()
    except:
        print('ERROR!!! File is empty.')
        
    
if __name__=='__main__':
    recfile = input('Enter filename whose records are to be sorted : ')
    RecordSave(recfile)
    sortfile = input('Enter filename in which sorted records are to be stored :')
    CreateIntermediateFiles.CreateIntermediateFiles(recfile)
    MergeFiles.MergeFiles(sortfile)
  
    choice='Y'
    while choice=='Y' or choice=='y':
        filename=input('Enter file name from which records are to be retrieved ')
        s=int(input('Enter start record number : '))
        e=int(input('Enter end record number : '))
        RangeRecords(filename,s,e)
        choice=input('Do you want to continue?(Y/y) : ')
        
    
    
   
    
                                 
                        

    
