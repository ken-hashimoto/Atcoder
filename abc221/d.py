N = int(input())
event = []
for _ in range(N):
  a,b = map(int,input().split())
  event.append((a,'in'))
  event.append((a+b,'out'))

event.sort()
ans = [0]*(N+1)
cnt = 0
for i in range(2*N):
  now,cond = event[i]
  if i == 0:
    prev = now
    cnt += 1
    continue
  ans[cnt] += now - prev
  prev = now
  if cond =='in':
    cnt += 1
  if cond == 'out':
    cnt -= 1
print(*ans[1:])

