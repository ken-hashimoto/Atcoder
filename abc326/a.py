x, y = map(int, input().split())
d = y - x
if d >= 0 and d <= 2:
    print("Yes")
    exit()
if d < 0 and -3 <= d:
    print("Yes")
    exit()

print("No")
