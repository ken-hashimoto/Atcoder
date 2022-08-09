N = int(input())
S = set()
ans = 0
zahyou = []
for i in range(N):
  x,y = map(int,input().split())
  S.add((x,y))
  zahyou.append((x,y))
for i in range(N):
  for j in range(N):
    xi,yi = zahyou[i]
    xj,yj = zahyou[j]
    #zahyou[i]がzahyou[j]の左上にあるとき
    if xi < xj and yi > yj:
      if (xi,yj) in S and (xj,yi) in S:
        ans += 1
        continue
print(ans)