import time

'''fish=['dory', 'bruce', 'marlin', 'nemo']
nemo=['nemo']
everyone=['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = ['nemo' for x in range(100000000 )]

def findNemo(arr):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i]=='nemo':
            break
            #print ("find Nemo")
    print("--- %s seconds ---" % (time.time() - start_time))
            
#findNemo(nemo)
#findNemo(fish)
#findNemo(everyone)
findNemo(large)

----------------------------------------------
box=[x for x in range(10)]

def logbox(n,arr):
    start=time.time()
    print (arr[n])
    print("--- %s seconds ---" % (time.time() - start))
    
    
logbox(0,box)
logbox(2,box)
logbox(4,box)
logbox(6,box)
logbox(8,box)
-----------------------------------------------
boxes=['a','b','c','d','e']

def printAllPairsOfArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print (arr[i]+arr[j])
            
printAllPairsOfArray(boxes)


arr=['hi','my','teddy']
print (arr[0])
print (arr[len(arr)-1]) 


----------------------------------------

#given 2 arrays, create a funtion that let's a user know(true false) whther these two array contains any common items


def compArray(arr1,arr2):
    
    start_time = time.time()
    'Elimina duplicados'
    a=set(arr1)
    b=set(arr2)
    
    #print(a)
    #print(b)
    
    'Compara si hay valores iguales'
    
    #print(a.intersection(b))
    if a.intersection(b)!= set():
        print("--- %s seconds ---" % (time.time() - start_time))
        return True
    print("--- %s seconds ---" % (time.time() - start_time))
    return False
  
def compArray2(arr1,arr2):
    
    return set(arr1).intersection(set(arr2)) != set()


a1=['a','b','c','x']
a2=['z','y','x']

print(compArray(a1,a2)) 
start_time = time.time()
print(compArray2(a1,a2))
print("--- %s seconds ---" % (time.time() - start_time))

-----------------------------------------------------

def hasPairwithSum(arr,suma):
    mySet=set(arr)
    
    for i in range(len(arr)):
        if suma-arr[i] in mySet:
            return True
    
    return False

hasPairwithSum([6,4,1,7],9)'''

    
    


