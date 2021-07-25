def maxDepth(s):
        """
        :type s: str
        :rtype: int
        """
        
        
        
        max=0
        current_max=0
        
        for i in s:
            
            if i =='(':
                current_max+=1
                


            if current_max > max :
                print(current_max)
                max=current_max
            
            if i ==')':
                current_max-=1
        print(max)        

maxDepth('(1)+((2))+(((3)))')