class Node():
    
    def __init__(self,value):
        self.value = value
        self.prev=None
        self.next=None
        
class DoubleLinkedList():
    
    def __init__(self,value):
        self.head=Node(value)
        self.tail=self.head
        self.lenght=1
        
    def append(self,value):
        newNode=Node(value)
        newNode.prev=self.tail
        self.tail.next=newNode
        self.tail=  newNode
        self.lenght+=1
        return self
    
    def prepend(self,value):
        newNode=Node(value)
        newNode.next=self.head
        self.head.prev=newNode
        self.head=newNode
        self.lenght+=1
        return self
    
    def printList(self):
        arr=[]
        currentNode=self.head
        while currentNode!=None:
            arr.append(currentNode.value)
            currentNode=currentNode.next
        return arr
    
    def insert(self,index,value):
        if index >= self.lenght:
            return self.append(value)
        newNode=Node(value)
        leader =  self.traverseToIndex(index-1)
        follower=leader.next
        leader.next=newNode
        newNode.prev=leader
        newNode.next=follower
        follower.prev=newNode
        self.lenght+=1
        return self.printList()
        
    def traverseToIndex(self,index):
        counter=0
        currentNode=self.head
        while counter!= index:
            currentNode=currentNode.next
            counter+=1
        return currentNode    
    
myLinkedList = DoubleLinkedList(10)
print(myLinkedList.printList())
myLinkedList.append(5)
print(myLinkedList.printList())
myLinkedList.append(16)
print(myLinkedList.printList())
myLinkedList.prepend(1)
print(myLinkedList.printList())
myLinkedList.insert(2, 99)
print(myLinkedList.printList())