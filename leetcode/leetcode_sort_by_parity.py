
def sort_by_parity(nums):

    eve=0
    odd=0

    for i in nums :
        if i %2 == 0:
            eve+=1
        else:
            odd+=1
    

    for i in range(eve):

        if nums[i] % 2 !=0 :
            for j in range(eve,len(nums)):
                if nums[j] % 2 ==0:
                    nums[j] , nums[i] = nums[i] , nums[j]
        
    
    print(nums)
            

sort_by_parity([3,1,2,4])

