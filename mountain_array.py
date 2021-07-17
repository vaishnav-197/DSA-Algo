def validMountainArray( arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        m=0
        if len(arr)<3:
            return 0
        
        for i in range(len(arr)-1):
            
            if arr[i]==arr[i+1]:
                return False
            if arr[i]<arr[i+1]:
                m+=1
            elif arr[i]>arr[i+1]:
                m-=1
                
        if m==0-len(arr)-1 or  m==len(arr)-1:
            return False
        
        up=0
        down=0
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                print("up")
                up=+1
            if arr[i-1]>arr[i] and arr[i]<arr[i+1]:
                print("down")
                down=+1
            
        if up ==1 and down==0:
            return True
        else :
            return False
        return False
v=validMountainArray([1,1,1,1,1,1,1,2,1])
print(v)