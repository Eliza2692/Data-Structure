class Queue(object):
    
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]
    
    def enqueue(self,item):
        self.items.append()
        
    def dequeue(self,item):
        self.items.pop(0)
    
    def size(self):
        return len(self.items )