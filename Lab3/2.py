def zero(m):
    k = 0
    for n in range(len(m)):
        if m[n] == 0:
            k += 1
    return k
a = []
k = 0
while k < 10:        #ввод с клавиатуры массива из 10 чисел
    x = int(input("Число:"))
    a.append(x)
    k += 1
print(zero(a))