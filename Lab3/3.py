n = int(input())
k = 0 
x = 0 
s = 0
while k <= n:
    while x < k:
        s = s*10 + (x+1)
        x += 1
        print(s)
    k += 1