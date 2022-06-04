import heapq
N,K = map(int,input().split())
A = list(map(int,input().split()))
li = []
for i in range(K):
  d = []
  heapq.heapify(d)
  li.append(d)
for i in range(N):
  heapq.heappush(li[i%K],A[i])
A_sort = sorted(A)
for i in range(N):
  r = i%K
  if A_sort[i] != heapq.heappop(li[r]):
    print('No')
    exit()
print('Yes')