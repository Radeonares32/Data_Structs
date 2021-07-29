def toplama(x,y):
    if y == 0:
        return 0
    return x + toplama(x,y-1)

def power(a,b):
    if b == 0:
        return 1
    return toplama(a,power(a,b-1))

print(power(2,3))