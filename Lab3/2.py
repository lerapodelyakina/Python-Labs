def zero(m):
    k = 0
    for n in range(len(m)):
        if m[n] == 0:
            k += 1
    return k
a = []
c = 0
while c < 10:           #ввод с клавиатуры массива из 10 чисел
    x = int(input("Число:"))
    a.append(x)
    c += 1
print(zero(a))