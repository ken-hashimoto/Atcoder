import heapq

Q = int(input())
M = []
heapq.heapify(M)
m = []
heapq.heapify(m)
d = dict()
for _ in range(Q):
  query = list(map(int,input().split()))
  n = query[0]
  if n == 1:
    x = query[1]
    if not x in d.keys():
      d[x] = 1
    else:
      d[x] += 1
    heapq.heappush(M,-x)
    heapq.heappush(m,x)
  if n == 2:
    x,c = query[1],query[2]
    if not x in d.keys():
      continue
    d[x] = max(0,d[x]-c)
  if n == 3:
    m_cand = heapq.heappop(m)
    while d[m_cand] <= 0:
      m_cand = heapq.heappop(m)
    heapq.heappush(m,m_cand)
    M_cand = -heapq.heappop(M)
    while d[M_cand] <= 0:
      M_cand = -heapq.heappop(M)
    heapq.heappush(M,-M_cand)
    print(M_cand - m_cand)