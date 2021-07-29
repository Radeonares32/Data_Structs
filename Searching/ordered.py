


def OrderedList(list,value):
    index = 0
    found = False
    stop = False
    while index < len(list) and not found and not stop:
        if list[index] == value:
            found = True
        else:
            if value < list[index]:
                stop = True
            else:
                index +=1
    return (found,index)

liste = [1,2,3,4,5,8,10]

found,index = OrderedList(liste,8)
print(found)
print(index)