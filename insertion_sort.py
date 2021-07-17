def insertion_sort(arr):
    for i in range(1,len(arr)):

        key = arr[i]
        j=i-1
        
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            
            j-=1
        arr[j+1]=key
        
        
    return arr

print(insertion_sort([1,3,5,2,5,3,4,5]))

