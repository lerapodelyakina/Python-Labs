list = [18,5,2,6,15,84,6,3,4,15]
def new(a):
    max1 = a.index(max(a))
    min1 = a.index(min(a))
    a[max1], a[min1] = a[min1], a[max1]
    print(a)
new(list)

