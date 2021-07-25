def merge_interval(intervals):
    

    if intervals == []:
        return []

    result = []

    intervals.sort()

    
    for i in intervals:
        if result == []  or result[-1][1]<i[0]:
            result.append(i)
        
        else:
            result[-1][1]= max(result[-1][1],i[1])

    
    return result

    
    



merge_interval([[1,3],[2,6],[8,10],[15,18]])