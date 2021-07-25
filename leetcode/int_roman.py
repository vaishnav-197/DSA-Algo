def intToRoman( num):
        """
        :type num: int
        :rtype: str
        """
        roman_num=''
        digit=0
        while num //(10**digit) !=0:
            temp= (num//10**digit)%10
            if digit==0:
                if temp < 5:
                    if temp==4:
                        roman_num+='VI'
                    else:
                        roman_num+='I'*temp
                else:
                    if temp==9:
                        roman_num+='XI'
                    else:
                        roman_num+=('I'*(temp%5)+'V')
            elif digit ==1:
                if temp < 5:
                    if temp==4:
                        roman_num+='LX'
                    else:
                        roman_num+='X'*temp
                else:
                    if temp==9:
                        roman_num+='CX'
                    else:
                        roman_num+=('X'*(temp%5)+'L')
            elif digit ==2:
                if temp < 5:
                    if temp==4:
                        roman_num+='DC'
                    else:
                        roman_num+='C'*temp
                else:
                    if temp==9:
                        roman_num+='MC'
                    else:
                        roman_num+=('C'*(temp%5)+'D')
            elif digit ==3:
                roman_num+='M'*temp
            
            digit+=1

        return roman_num[::-1]

print(intToRoman(25))