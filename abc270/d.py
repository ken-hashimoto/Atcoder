N,K = map(int,input().split())
A = list(map(int,input().split()))
#takahashi[i] = (i個の石でゲームした時のtakahashi君が取り除ける医師の最大)
takahashi = [-1 for _ in range(10010)]
takahashi[0] = 0
takahashi[1] = 1
ans = 0
for i in range(2,N+1):
  for j in range(K):
    if i - A[j] >= 0:
      aoki = takahashi[i - A[j]]
      takahashi[i] = max(takahashi[i],i - aoki)
    else:
      break
print(takahashi[N])