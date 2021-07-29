def toplama(x,y):
    if y == 0:
        return 0
    return x + toplama(x,y-1)

print(toplama(2,3))
 