def selection_sort(arr):
    for i in range(len(arr)-1,0,-1):
        maxValue = 0
        for location in range(1,i+1):
            if arr[location] > arr[maxValue]:
                maxValue = location
        print(maxValue)
        tmp = arr[i]
        arr[i] = arr[maxValue]
        arr[maxValue] = tmp
    return arr
data=selection_sort([3,5,7,1,20,32,4])
print(data)