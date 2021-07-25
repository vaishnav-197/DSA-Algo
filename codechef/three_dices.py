t= int(input())

answer=[]

for i in range (t):
    x, y = map(int, input().split())

    if x+y >=6:
        answer.append(0)
    else:
        answer.append((6-(x+y))/6)

for i in answer:
    print(i)