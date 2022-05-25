N,M = map(int,input().split())
cnt_li = [0 for _ in range(N+1)]
ans = 0
for i in range(M):
  a,b = map(int,input().split())
  if a < b:
    cnt_li[b] += 1
  if a > b:
    cnt_li[a] += 1
for i in range(1,N+1):
  if cnt_li[i] == 1:
    ans += 1
print(ans)
