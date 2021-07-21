t= int(input())


answer=[]
for i in range (t):
    D, d, P, Q = map(int, input().split())
    n = D//d
    ans = n*P*d + (Q*(n*(n-1))//2)*d +(D%d)*(P+n*Q)
    answer.append(ans)

for i in answer:
    print(i)


