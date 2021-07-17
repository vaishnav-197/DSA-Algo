t= int(input())
d=dict()
for j in range(t):
    n,k=map(int,input().split())
    s=input()
    
    gs=0
    e=n-1
    for i in range((n//2)):
        if s[i]!=s[e]:
            gs+=1
            
        e-=1
    d[j]=abs(k-gs)

for i in d:
    print("Case #{}: {}".format(i+1,d[i]))

