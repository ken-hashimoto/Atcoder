N,K = map(int,input().split())
scores = []
for _ in range(N):
  A,B = map(int,input().split())
  scores.append(B)
  scores.append(A-B)
scores.sort(reverse=True)
print(sum(scores[:K]))
