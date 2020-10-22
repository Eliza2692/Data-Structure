class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
        
def cycle_check(node):
    
    x=node
    y=node.nextnode
    while y != None:
        if y.value==node.value:
            return True
        else :
            x=y
            y=x.nextnode
    return False

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

print (cycle_check(a))

print (cycle_check(x))