import numpy, pickle, random

class Record:
    '''
    A class to represent the record.
    '''

    def __init__(self,key,nonKey):
        '''
        Objective        : To inititalize an object of the class Record.
        Input Parameters :
           self(Implicit parameter)-> Object of type Record
                               key -> The key attribute of the record.
                            nonKey -> The non-key attribute of the record.
        Output           :  None
        '''
        self.key = key
        self.nonKey = nonKey

    def __str__(self):
        '''
        Objective        : To return a string representation of the object of Record class.
        Input Parameters :
           self(Implicit parameter)-> Object of type Record
        Output           : String representation of the given record.
        '''
        return 'KEY :'+str(self.key) + ' NON-KEY : '+str(self.nonKey)

def RecordKey(record):
    '''
    Objective        : To get the key attribute of the given record.
    Input Parameters :
             record -> The record whose key we have to find.
    Output           : The key attribute of the given record.
    '''
    return record.key

def createDataFile(noOfRecords):
    '''
    Objective        : To create a data file of given no. of records.
    Input Parameters :
        noOfRecords -> Number of records.
    Output           : None
    '''
    dataFile = open('dataFile.bin','wb')
    minKey, threshold = 1, 100000
    allKeys = random.sample(range(minKey,(minKey+noOfRecords)*4),noOfRecords)
    for key in allKeys:
        key = numpy.int64(key)
        nonKey = str(key+threshold) * 5
        pickle.dump(Record(key,nonKey),dataFile)
    dataFile.close()
    createDataPosFile()

def createDataPosFile():
    '''
    Objective : To create a data position file which contains a list of starting positions of all the records in the data file.
    Input     : None
    Ouput     : None
    '''
    dataPosList = []
    dataFile = open('dataFile.bin','rb') 
    while True:
        dataPosList.append(dataFile.tell())
        try:
            pickle.load(dataFile)
        except:
            break
    dataFilePos = open('dataPosFile.bin','wb') 
    pickle.dump(dataPosList,dataFilePos)
    dataFilePos.close()
    dataFile.close()

def printFile(fileName):
    '''
    Objective        : To print the entire given file.
    Input Parameters :
           filename -> Name of the file whose contents are to be printed.
    Output           : None
    '''
    file = open(fileName,'rb') 
    while True:
        try:
            print(pickle.load(file))
        except EOFError:
            break

def printFileInRange(fileName, first, last):
    '''
    Objective        : To print the data in the given file within the given range.
    Input Parameters :
        filename -> Name of the file whose contents are to be printed.
        first    -> First record no.
        last     -> Last record no.
    Output           : None
    '''
    file = open(fileName,'rb') 
    pickle.load(file)
    size = file.tell()
    
    while first<=last:
        file.seek(size * (first-1))
        try:
            print(pickle.load(file))
            first += 1
        except EOFError:
            break

def fetchRecord(fileName,index):
    '''
    Objective        : To fetch a record from the given location.
    Input Parameters :
           filename -> Name of the file from which record is to be fetched..
           location -> The index of the record in given file.
    Output           : None
    '''
    dataPosFile = open('dataPosFile.bin','rb') 
    dataPosList = pickle.load(dataPosFile)
    dataFile = open('dataFile.bin','rb') 
    dataFile.seek(dataPosList[index])
    return pickle.load(dataFile)
    

    
            
        
        
