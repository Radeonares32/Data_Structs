def array_pair(array):
    new = ""
    for k in range(len(array)):
        new += str(array[k]) + " "
        if(k%2==1):
            new += ","
    new = new.split(' ,')
    depo = []
    for i in new:
        if i[::-1] not in new:
            for l in i.split():
                depo.append(l)
        elif i==i[::-1] and new.count(i)<2:
            for j in i.split():
                depo.append(j)
    if depo == []:
        return "okay"
    return ",".join(depo) 

x = array_pair([1,5,5,1,4,4,4,4])
print(x)