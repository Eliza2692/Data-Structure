def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for i in range(0,len(arr1)-1):
        if arr1[i]!=arr2[i]:
            lost=arr1[i]
            break
    return lost


arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(finder(arr1,arr2))