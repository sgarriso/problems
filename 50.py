def merge(arr1=[1,3,5],arr2=[2,4,6]):
    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = [None] * (n1 + n2) 
    i = 0
    j = 0
    k = 0
  
    # Traverse both array 
    while i < n1 and j < n2: 
      
        # Check if current element  
        # of first array is smaller  
        # than current element of  
        # second array. If yes,  
        # store first array element  
        # and increment first array 
        # index. Otherwise do same  
        # with second array 
        if arr1[i] < arr2[j]: 
            arr3[k] = arr1[i] 
            k = k + 1
            i = i + 1
        else: 
            arr3[k] = arr2[j] 
            k = k + 1
            j = j + 1
      
  
    # Store remaining elements 
    # of first array 
    while i < n1: 
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1
  
    # Store remaining elements  
    # of second array 
    while j < n2: 
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1
    return arr3
def is_even(n):
    return n % 2 == 0
def find_median(arr):
    answer = None
    right = int(len(arr)/2)
    if is_even(len(arr)):
        left = int(len(arr)/2-1)
 
        answer = (arr[left] + arr[right]) // 2
    else:
        answer = arr[right]
    return answer
        
    
def median(arr2=[1],arr1=[2,4,6]):
    arr = merge(arr1,arr2)
    answer=find_median(arr)
    return answer
    
print(median())
    
