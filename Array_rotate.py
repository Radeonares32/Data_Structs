def array_rotate(array):
    eski_index = array[0]
    yeni_index = [str(array[eski_index])]
    counter = eski_index + 1
    lenght = len(array)
    while counter%lenght != eski_index:
        yeni_index.append(str(array[counter%lenght]))
        counter +=1
    return "".join(yeni_index)


x = array_rotate([2,3,4,5,6])
print(x)