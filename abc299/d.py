N = int(input())
zero = 0
one = N - 1
while abs(zero - one) > 1:
    m = (zero + one) // 2
    print("? " + str(m + 1), flush=True)
    res = int(input())
    if res == 0:
        zero = m
    else:
        one = m
print("! " + str(zero + 1))
