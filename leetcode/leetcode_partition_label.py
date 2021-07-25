


def partition_labels(s):

    d={}
    res=[]

    for i in range(len(s)):
        if  s[i] in d:
            d[s[i]]=i

        else:
            d[s[i]]=i


    


    b=0
    e=d[s[0]]
    for i in range(len(s)):
        # print(e)
        if i == e:
            # print(e)
            res.append(len(s[b:e+1]))
            if i==len(s)-1:
                break
            else:
                b=i+1
                e=d[s[i+1]]

        
        if d[s[i]] > e:
            e=d[s[i]]
    
    return res
        


print("input","caedbdedda")
print(partition_labels("caedbdedda"))
        