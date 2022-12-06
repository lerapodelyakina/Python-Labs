list = [1,5,2,6,15,84,6,3,4,15]
def new(a):
    b = []
    for i in range(len(a)):
        if a[i] > a[i - 1]:
            b.append(a[i])
    return b
print(new(list))

