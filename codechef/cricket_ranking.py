t= int(input())

answer=[]
inp=[]
for i in range (t*2):
    k = list(map(int, input().split()))
    inp.append(k)

i=0

while i < t*2:
    a=0
    b=0

    if  inp[i][0] > inp[i+1][0]:
        a+=1
    else :
        b+=1
        
    if  inp[i][1] > inp[i+1][1]:
        a+=1
    else :
        b+=1
    
    if  inp[i][2] > inp[i+1][2]:
        a+=1
    else :
        b+=1
    

    if a>b:
        answer.append('A')
    else:
        answer.append('B')
    
    i+=2

for i in answer:
    print(i)



