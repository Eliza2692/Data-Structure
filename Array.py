"""ARRAYS________________________________________"""

class myArray:
    
    def __init__(self):
        self.lenght=0
        self.data={}
        
    def get(self,index):
        return self.data[index]
    
    def push(self,item):
        self.data[self.lenght]=item
        self.lenght+=1
        return self.data
    
    def pop(self):
        lastItem=self.data[self.lenght-1]
        del self.data[self.lenght-1]
        self.lenght-=1
        return lastItem
    
    def shiftItems(self,index):
        for i in range(index,self.lenght-1):
            self.data[i]=self.data[i+1]
        print(self.data[self.lenght-1])
        del self.data[self.lenght-1]
        self.lenght-=1
        
    def deleteAtIndex(self,index):
        item=self.data[index]
        self.shiftItems(index)
        return item


myArr = myArray()
myArr.push('hi')
myArr.push('you')
myArr.push('!')
myArr.pop()
myArr.deleteAtIndex(0)
myArr.push('are')
myArr.push('nice')
myArr.shiftItems(0)
print(myArray)
myArr



def reverse(s):
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 

print(reverse("hi My name is Andrei"))


def mergeSotedArrays(arr1,arr2):
    
    mergedArray=[]
    len1=len(arr1)
    len2=len(arr2)
    
    #organize the array 1
    for i in range(len1):
 
        for j in range(0, len1-i-1):

            if arr1[j] > arr1[j+1] :
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
                
    #organize the array 1
    for i in range(len2):
 
        for j in range(0, len2-i-1):

            if arr2[j] > arr2[j+1] :
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]

    #fill the merged array and compare
    i,j=0,0
    
    while i<len1 and j<len2:

        if arr1[i]<arr2[j]:
            mergedArray.append(arr1[i])
            i+=1
            
        else:
            mergedArray.append(arr2[j])
            j+=1 

    if i<len1:
        for x in range(i,len1):
            mergedArray.append(arr1[x])
    else:
        for x in range(j,len2):
            mergedArray.append(arr2[x])
            
    print (mergedArray)
    return mergedArray

mergeSotedArrays([0,23,4,31], [4,10,30,7])

