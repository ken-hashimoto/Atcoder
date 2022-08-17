N = int(input())
C = list(map(int,input().split()))
m = min(C)
keta = N//m
ans = []
k = 0
while True:
  num = -1
  for i in range(9):
    if C[i] <= N:
      if N - C[i] >= m*(keta-k-1):
        num = i+1
  if num == -1:
    break
  N -= C[num-1]
  ans.append(str(num))
  k += 1
print(''.join(ans))