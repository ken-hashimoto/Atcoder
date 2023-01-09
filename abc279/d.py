def f(x):
    global A, B
    return B * x + A / ((x + 1) ** 0.5)


A, B = map(int, input().split())
l = 0
r = 10**18
while abs(l - r) > 2:
    c1 = (2 * l + r) / 3
    c2 = (l + 2 * r) / 3
    if f(c1) > f(c2):
        l = c1
    elif f(c1) < f(c2):
        r = c2
    elif f(c1) == f(c2):
        l = c1
        r = c2
l = l // 1
ans = [f(l), f(l + 1), f(l + 2), f(l + 3)]
print(min(ans))
