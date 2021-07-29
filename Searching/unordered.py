def UnOrderedList(list,value):
    index = 0
    found = False
    while index < len(list) and not found:
        if list[index] == value:
            found = True
        else:
            found = False
            index +=1
    return (found,index)

liste = [1,2,3,4,5,6,7,8,9,10]

index,found =  UnOrderedList(liste,5)

print(index)
print(found)