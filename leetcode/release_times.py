def slowestKey(releaseTimes,keysPressed): 
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        x = [i for i in keysPressed]
        down =0
        for i in range(len(releaseTimes)):
            temp=releaseTimes[i]-down
            down=releaseTimes[i]
            releaseTimes[i]=temp
        maximum =max(releaseTimes)
        
        map=[]
        for i in range(len(releaseTimes)):
            if releaseTimes[i]==maximum:
                map.append(i)
        res=[]
        for i in range(len(x)):
            if i in map:
                res.append(x[i])
        return max(res)
            
            
        
slowestKey([9,29,49,50] , "cbcd")