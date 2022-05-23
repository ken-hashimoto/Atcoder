N,W = map(int,input().split())
A = list(map(int,input().split()))
S = set()
for i in range(N):
  weight = A[i]
  if weight <= W:
    S.add(weight)
  for j in range(i+1,N):
    weight = A[i] + A[j]
    if weight <= W:
      S.add(weight)
    for k in range(j+1,N):
      weight = A[i] + A[j] + A[k]
      if weight <= W:
        S.add(weight)
print(len(S))