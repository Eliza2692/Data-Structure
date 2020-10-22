import ctypes

class DynamicArray(object):
    
    def _init_(self):
        self.n=0
        self.capacity=1
        self.A = self.make_array(self.capacity)
        
    def _len_(self):
        return self.n
    
    def _getitem_(self,k):
        if not 0 <= k < self.n:
            return IndexError ("K is out of bpounds!")
        return self.A[k]
        
    def make_array(self,new_cap):
        return (new_cap*ctypes.py_object)()
    
    def _resize_(self, new_cap):
        B= self.make_array(new_cap)
        for k in range(self.n):
            B[k]=self.A[k]
        self.A=B
        self.capacity=new_cap
    
    def append(self,ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n]=ele
        self.n +=1
        
    
    
arr=DynamicArray()

arr.append(3)
print (len(arr))

arr.append(6)
print (len(arr))

