def summa(m):
    return sum(m)
k = 0
a = []
while k < 5:            #цикл для введения с клавиатуры масссива из 10 элементов
    x = int(input())
    a.append(x)
    k += 1

print(summa(a))