

class Node():

    def __init__(self,value):
        self.value = value
        self.next = None



class Stack():
      
    
    def __init__(self):
        self.top = None
        self.bottom = None
        self.lenght = 0
    
    
    def peek(self):
        if self.isEmpty():
            return "None"
        return self.top.value
            
    
    def push(self,value):
        
        newNode = Node(value)
        
        if self.lenght==0:
            self.top=newNode
            self.bottom = newNode
        else:
            
            newNode.next = self.top
            self.top = newNode
        
        self.lenght +=1
        
        return self
    
    
    def pop(self):
        
        value = self.top.value
        self.top = self.top.next
        
        return value
    
    
    def isEmpty(self):
        return not self.top



class StackArray():
    
    
    def __init__(self):
        self.items = []


    def peek(self):
        if self.isEmpty():
            return "None"
        return self.items[len(self.items)-1]
            
    
    def push(self,value):
        
        self.items.append(value)
        
        return self
    
    
    def pop(self):
        
        return self.items.pop()
    
    
    def isEmpty(self):
        return self.items == []


    
class Queue():
    
    
    def __init__(self):
        self.top = None
        self.bottom = None
        self.lenght = 0
    
    
    def peek(self):
        if self.isEmpty():
            return "None"
        return self.top.value


    def enqueue(self,value):
        
        newNode = Node(value);
        if self.lenght==0:
            self.top=newNode
            self.bottom = newNode
        else:
            self.bottom.next=newNode
            self.bottom=newNode
        
        self.lenght +=1
        
        return self
    
    
    def dequeue(self):
        
        value = self.top.value
        self.top = self.top.next
        
        return value
    
    
    def isEmpty(self):
        return not self.top
    

class QueueArray():
    
    
    def __init__(self):
        self.items = []


    def peek(self):
        if self.isEmpty():
            return "None"
        return self.items[0]
            
    
    def enqueue(self,value):
        
        self.items.append(value)
        
        return self
    
    
    def dequeue(self):
        
        return self.items.remove(self.items[0])
    
    
    def isEmpty(self):
        return self.items == []  
    
"""myStack =Stack()
print(myStack.peek())
myStack.push('google')
print(myStack.peek())
myStack.push('udemy')
print(myStack.peek())
myStack.push('discord')
print(myStack.peek())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())


myStack =StackArray()
print(myStack.peek())
myStack.push('google')
print(myStack.peek())
myStack.push('udemy')
print(myStack.peek())
myStack.push('discord')
print(myStack.peek())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())"""


myQueue = QueueArray()
print(myQueue.peek())
myQueue.enqueue('Joy')
print(myQueue.peek())
myQueue.enqueue('Matt')
print(myQueue.peek())
myQueue.enqueue('Pavel')
print(myQueue.peek())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.peek())