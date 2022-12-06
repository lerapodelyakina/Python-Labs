list = [1,2,3,4,5]
def new(a):
    b = []
    for index in a:
        if index % 2 == 0 and index != 0:
            b.append(a[index])
    return b
print(new(list))

