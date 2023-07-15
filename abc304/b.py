N = int(input())
if N < 10**3:
    print(N)
    exit()
k = 2
while True:
    if 10**(k+1) <= N:
        k += 1
    else:
        break

k -= 3
print((N // 10**k)*10**k)