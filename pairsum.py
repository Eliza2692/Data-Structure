def pair_sum(arr,k):
    """pair=0
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if isinstance(j, int) and (i/1)==i:
                suma=(arr[i]+arr[j])
                if suma==k:
                    pair+=1 
    return pair"""
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        target = k-num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        
        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
    
    
    # FOR TESTING
    return len(output)
print (pair_sum([1,3,2,2],4))