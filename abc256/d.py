N = int(input())
zahyou = []
ans = []
for i in range(N):
  L,R = map(int,input().split())
  zahyou.append((L,R))
zahyou.sort()

for i in range(N):
  l,r = zahyou[i]
  if i == 0:
    tmp = (l,r)
    continue
  if l > tmp[1]:
    ans.append(tmp)
    tmp = (l,r)
  else:
    tmp = (min(tmp[0],l),max(tmp[1],r))
ans.append(tmp)

ans.sort()
for answer in ans:
  print(*answer)