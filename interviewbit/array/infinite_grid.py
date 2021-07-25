
def coverPoints( A, B):
        
        if len(A)==1 or len(A)==0:
            return 0

        min = 0
        for i in range(len(A)-1):
            min+= max(abs(A[i]-A[i+1]),abs(B[i]-B[i+1]))

        return min

print(coverPoints([ -7, -13 ],[-1,-5]))