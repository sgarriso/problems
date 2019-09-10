def suma(num,k):
    data = {}
    for i in range(0,len(num)):
        c = k - num[i]
        if c in data.keys():
            return True
        data[num[i]]=i
    return False
        

def products(nums):
    
    length = len(nums)
    ans = [0] * length
    ans[0] = 1
    for i in range(1,length):
        ans[i] = nums[i-1] * ans[i-1]
    r = 1
    for i in reversed(range(length)):
        ans[i] = ans[i] * r
        r *= nums[i]
    return ans

print(products([1, 2, 3, 4, 5]))
                      
    
    
