N = int(input())
r = N%5
if r >= 3:
    print(N + (5-r))
else:
    print(N - r)