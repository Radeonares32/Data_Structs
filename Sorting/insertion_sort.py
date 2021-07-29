def insertion(arr):
    for i in range(len(arr)):
        current_value = arr[i]
        position = i
        while position > 0 and arr[position-1] > current_value:
            arr[position] = arr[position-1]
            position -= 1
        arr[position] = current_value
    return arr

liste = [1,5,9,8,7,20,35]

result = insertion(liste)

print(liste)