b = int(input())
a = 1
while a**a <= b:
    if a**a == b:
        print(a)
        exit()
    a += 1
print(-1)
