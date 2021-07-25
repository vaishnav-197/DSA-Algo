


t= int(input())
inpt=[]
inp=[]
for i in range(t):
    inp=list(map(int,input().split())) 
    inpt.append(inp)


for i in range(t):
    num = (inpt[i][2])//(inpt[i][0]) + (inpt[i][3])//(inpt[i][1])
    print(num)

