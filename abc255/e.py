import collections
N,M = map(int,input().split())
S =  list(map(int,input().split()))
X = list(map(int,input().split()))
B = []
prev = 0
for i in range(N):
  if i == 0:
    B.append(prev)
  else:
    s = S[i-1] - prev
    B.append(s)
    prev = s
C = []
for i in range(N):
  for j in range(M):
    c = (X[j] - B[i]) * (-1)**(i+1)
    C.append(c)
cnt = collections.Counter(C)
ans = max(cnt.values())
print(ans)