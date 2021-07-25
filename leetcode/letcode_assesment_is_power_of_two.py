def is_Power_of_Two(n):

    
    while(n>0):

        
        if n%2 !=0:
            return False
        n=n/2
        
        return True

print(is_Power_of_Two(2))