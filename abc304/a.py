N = int(input())
names = []
min_name = 0
min_age = float('INF')
for i in range(N):
    s,a = input().split()
    a = int(a)
    if a < min_age:
        min_age = a
        min_name = s
    names.append(s)
ind = names.index(min_name)
for i in range(N):
    print(names[(ind+i)%N])
