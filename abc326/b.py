n = int(input())
k = n
while True:
    a = k // 100
    b = (k % 100) // 10
    c = k % 10
    if a * b == c:
        print(k)
        exit()
    k += 1
