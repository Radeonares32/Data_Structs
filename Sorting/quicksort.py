def quicksort(arr):
    quicksort_recursion(arr,0,len(arr)-1)
    return arr
def quicksort_recursion(arr,first,last):
    if first < last:
        splitpoint = partition(arr,first,last)
        quicksort_recursion(arr,first,splitpoint-1)
        quicksort_recursion(arr,splitpoint+1,last)
def partition(arr,first,last):
    # pivot value => ilk eleman
    pivotvalue = arr[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while left <= right and arr[left] <=pivotvalue:
            left = left + 1
        while arr[right] >= pivotvalue and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
    temp = arr[first]
    arr[first] = arr[right]
    arr[right] = temp
    return right



arr = [3,2,13,4,5,7,75]
dv = quicksort(arr)
print(dv)