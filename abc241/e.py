N,K = map(int,input().split())
G = [-1 for i in range(N)]
A = list(map(int,input().split()))
now = 0
next = 0
tmp = 0
trace = []
candy = []
for i in range(N+10):
  if G[now] != -1:
    start = now
    break
  trace.append(now)
  next += A[now]
  next %= N
  tmp += A[now]
  candy.append(A[now])
  if i == K-1:
    print(tmp)
    exit()
  G[now] = next
  now = next
start_ind = trace.index(start)
candy_cnt_to_start = sum(candy[:start_ind])
period = len(trace) - start_ind
candy_cnt_from_start = candy[start_ind:]
candy_cnt_period = sum(candy_cnt_from_start)
ans = candy_cnt_to_start
K -= start_ind
ans += candy_cnt_period * (K//period)
ans += sum(candy_cnt_from_start[:K%period])
print(ans)
