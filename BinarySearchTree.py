import random

class Node():   
    def __init__(self,value):
        
        self.left = None
        self.right = None
        self.value = value
    

    
class BinarySearchTree():
    
    
    def __init__(self):   
        
        self.root=None
        
        
    def insert(self,value):  
        if self.root == None:           
            self.root = Node(value)           
        else:           
            node = self.root         
            while True:               
                if value >= node.value:                   
                    if node.right == None:                       
                        node.right = Node(value)
                        
                        return self
                        
                    else:                       
                        node = node.right                       
                else:                   
                    if node.left == None:                       
                        node.left = Node(value)
                        
                        return self
                        
                    else:                       
                        node = node.left                        
        
        return self
    
                    
    def lookup(self,value):
        
        if self.root == None:
            
            return None
        
        elif value == self.root.value:
            
            return True
                       
        else:           
            node = self.root         
            while True:               
                if value >= node.value:                   
                    if node.right == None:                       
                        
                        return False
                    
                    elif node.right.value == value: 
                        
                        return True
                    
                    else:                       
                        node = node.right                       
                else:
                    
                    if node.left == None:                       
                        
                        return False
                    
                    elif node.left.value == value: 
                        
                        return True
                    
                    else:                       
                        node = node.left
                        
        return False
   
    '''def remove (self,value):
        
        node = self.root 
        
        if value != self.root.value :  
            
            node = self.root 
            found = False
            
            while not found:
                
                if value > node.value: 
                    node = node.right
                    if value == node.value:
                        found = True                      
                
                else:
                    node = node.left
                    if value == node.value:
                        found = True
        
        if node.left == None and node.right == None:
            node.value = None
            
        elif node.left != None and node.right == None: 
            node = node.left
            
        else:
            nodeR= node.right
            if nodeR.left == None:
                node = node.right
            else:
                sucesor = nodeR.left
                while sucesor.left != None:
                    sucesor = sucesor.left
                node
        
                    
            
            
        return self'''
            
                        

        
    
tree = BinarySearchTree();
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)


