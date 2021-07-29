def bul(string):
    for i in range(10):
        c = string.replace("x",str(i))
        x = string.index("=")
        if eval(c[:x]) == eval(c[x+1:]):
            return str(i)
print(bul("10-x=4"))
