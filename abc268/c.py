N = int(input())
P = list(map(int,input().split()))
dist = [[]*N]
for i in range(N):
  diff = (i - P[i])%N
  dist[diff].append(i) 
print(dist)