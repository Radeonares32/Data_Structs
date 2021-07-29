def merge_sort(arr):
    if len(arr) > 1:
        midd = int(len(arr)/2)
        lefthalf = arr[:midd]
        righthalf = arr[midd:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        lfti = 0
        rghi = 0
        arri = 0
        while lfti < len(lefthalf) and rghi < len(righthalf):
            if lefthalf[lfti] < righthalf[rghi]:
                arr[arri] = lefthalf[lfti]
                lfti +=1
            else:
                arr[arri] = righthalf[rghi]
                rghi +=1
            arri +=1
        while lfti < len(lefthalf):
            arr[arri] = lefthalf[lfti]
            lfti +=1
            arri +=1
        while rghi < len(righthalf):
            arr[arri] = righthalf[rghi]
            rghi +=1
            arri +=1
    return arr

liste = [3,6,9,1,5,9,7,0]
sort = merge_sort(liste)
print(sort)

