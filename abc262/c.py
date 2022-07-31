N = int(input())
A = list(map(int,input().split()))
li = [set() for _ in range(N+1)]
cnt = 0
ans = 0
for i in range(N):
  li[A[i]].add(i + 1)
  if A[i] == i+1:
    cnt += 1
ans += (cnt * (cnt-1) )//2
for i in range(1,N+1):
  for num in li[i]:
    if num > i:
      if i in li[num]:
        ans += 1
print(ans)