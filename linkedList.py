class Node():
    
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList():
    
    def __init__(self,value):
        self.head=Node(value)
        self.tail=self.head
        self.length=1
        
    def append(self,value):
        newNode=Node(value)
        self.tail.next=newNode
        self.tail=newNode
        self.length+=1
        return self
    
    def prepend(self,value):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode
        self.length+=1
        return self
     
    def printList(self):
        arr=[]
        currentNode=self.head
        while currentNode!=None:
            arr.append(currentNode.value)
            currentNode=currentNode.next
        return arr
              
    def insert(self,index,value):
        if(index>=self.length):
            return self.append(value)
        newNode=Node(value)
        leader=self.traverseToIndex(index-1)
        holdingPointer=leader.next
        leader.next=newNode
        newNode.next=holdingPointer
        self.length+=1
        return self.printList()
        
    def traverseToIndex(self,index):
        counter=0
        currentNode=self.head
        while counter!= index:
            currentNode=currentNode.next
            counter+=1
        return currentNode
    
    def remove(self,index):
        leader=self.traverseToIndex(index-1)
        unwanted=leader.next
        leader.next=unwanted.next
        self.length-=1
        return self.printList()
        
    def reverse(self):
        if not self.head.next:
            return self.head
        first=self.head
        self.tail=self.head
        second = first.next
        while second:
            temp1=second.next
            first=second
            second=temp1
        self.head.next=None
        self.head=first
        return self.printList()
    
        
myLinkedList = LinkedList(10)
print(myLinkedList.printList())
myLinkedList.append(5)
print(myLinkedList.printList())
myLinkedList.append(16)
print(myLinkedList.printList())
myLinkedList.insert(2, 99)
print(myLinkedList.printList())
myLinkedList.insert(20, 88)
print(myLinkedList.printList())
myLinkedList.remove(2)
print(myLinkedList.printList())
myLinkedList.reverse()
print(myLinkedList.printList())

