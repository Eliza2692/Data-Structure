
class HashTable():
    
    def __init__(self,size):
        self.data=[None]*size
        
    def _hash(self,key):
        hash=0
        for i in range(len(key)):
            hash= (hash+ord(key[i])*i)%len(self.data)
            #print (hash)
        return hash
    
    def sets(self,key,value):
        adress=self._hash(key)
        if not self.data[adress]:
            self.data[adress]=[]
        self.data[adress].append([key,value])
        return self.data
    
    def get(self,key):
        adress=self._hash(key)
        currentBucket=self.data[adress]
        if currentBucket :
            for i in range(len(currentBucket)):
                if currentBucket[i][0]==key:
                    return currentBucket[i][1]
        return None
            

myHashTable= HashTable(50)
myHashTable.sets('grapes', 10000)
myHashTable.get('grapes')
myHashTable.sets('apples', 9)
myHashTable.get('apples')