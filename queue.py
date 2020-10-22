class Queue(object):
    
    def __init__(self):
      self.items=[]

    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items==[]
    
    def size(self):
        return len(self.items)
    
q=Queue()
print (q.size())
print (q.isEmpty())

q.enqueue("ola")
q.enqueue("como")

print (q.dequeue())
