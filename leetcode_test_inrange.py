def in_Range(nums):

    d={}

    for i in range(1,len(nums)+1):
        
        d[i]=0

    
    for i in nums:
        
        d[i]=1
    
    res=[]

    for i in d:
        if d[i]==0:
            res.append(i)
    
    return res



in_Range([4,3,2,7,8,2,3,1])
        