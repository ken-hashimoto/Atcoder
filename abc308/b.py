N,M = map(int,input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int,input().split()))

price = dict()
for i in range(M):
    price[D[i]] = P[i+1]
ans = 0
for i in range(N):
    c = C[i]
    if c not in price.keys():
        ans += P[0]
    else:
        ans += P[C]
print(ans)
