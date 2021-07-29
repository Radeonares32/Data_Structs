def bubblesort(array):
    for n in range(len(array)-1,0,-1):
        for k in range(n):
            if array[k] > array[k+1]:
                temp = array[k]
                array[k] = array[k+1]
                array[k+1] = temp
    return array

print(bubblesort([20,4,6,13,2,5,7,8]))