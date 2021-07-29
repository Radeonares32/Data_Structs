def BinarySearch(liste,value):
    first_index = 0
    last_index = len(liste)-1
    found = False
    while first_index <= last_index and not found:
        middle_index = int((first_index+last_index)/2)
        if liste[middle_index] == value:
            found = True
        else:
            if liste[middle_index] > value:
                last_index = middle_index -1
                print("Lower half")
            else:
                first_index = middle_index + 1
                print("Upper Half")
    return (found)


found = BinarySearch([2,4,6,8,20,23,40,53],6)
print(found)


