t= int(input())
d=dict()
for i in range(t):
    n,b=map(int,input().split())
    hp=list(input().split())
    hp = [int(x) for x in hp]
    hp.sort()
    
    h=0
    
    for k in hp:
        if b>=k:
            h+=1
            b-=k
    d[i]=h

for i in d:
    print("Case #{}: {}".format(i+1,d[i]))
