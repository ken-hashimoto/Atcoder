N = int(input())
A = []
for i in range(2*N-1):
  INPUT = [0]*(i+1) + list(map(int,input().split()))
  A.append(INPUT)
used = [False]*(2*N)

ans = 0
def dfs(pairs,tmp):
  if pairs == N:
    global ans
    ans = max(ans,tmp)
    return
  for i in range(2*N):
    if used[i] == False:
      used[i] = True
      break
  for j in range(i+1,2*N):
    if used[j] == False:
      used[j] = True
      dfs(pairs+1,tmp ^ A[i][j])
      used[j] = False
  used[i] = False

dfs(0,0)
print(ans)
  
