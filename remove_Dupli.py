
import string

def removeDuplicates( s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif i==stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        
        res = ''
        for i in stack:
            res+=i
        return res
res= removeDuplicates('azxxzy')
print(res)