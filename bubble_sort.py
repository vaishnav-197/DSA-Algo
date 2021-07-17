def bubble_sort(arr):
    for i in range(len(arr)-1):

        j=0

        while j< len(arr)-i-1:
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            j+=1
    
    return arr

print(bubble_sort([1,4,3,2,5,6,3,8]))