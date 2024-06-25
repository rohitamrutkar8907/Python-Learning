def multipleargd(*args):
    total=0
    for i in args:
        total= total+i
    return total
print(multipleargd(1,2,3))