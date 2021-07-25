class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n=len(digits)
        b=0
        if n==1 and digits[n-1]==9:
            digits[n-1]=0
            digits.insert(0,1)
            return digits
        elif digits[n-1]==9 :
            b=1
            digits[n-1]=0
            for i in range(n-2,-1,-1):
                if digits[i]!= 9:
                    digits[i]+=1
                    return digits

                elif i==0 and digits[i]==9 :
                    digits[0]=0
                    digits.insert(0,1)
                    return digits
                    
                elif digits[i]==9:
                    digits[i]=0
        else :
            digits[n-1]+=1
            return digits
        