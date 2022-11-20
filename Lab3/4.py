n = int(input())
for i in range(1, n+1):
    for p in range (n - i):
        print(" ", end = ' ')
    for s in range(1, i):
        print(s, end = ' ')
    for i in range(i, 0, -1):
        print(i, end = ' ')
    for p in range(n - i):
        print(" ", end=' ')
    print("\n")