import math
N = int(input())
if N == 1:
  print(1)
  exit()
prev = [1,1]
for i in range(1,N+1):
  if i == 1:
    print(1)
    continue
  if i == 2:
    print(1,1)
    continue
  ans = []
  for j in range(i):
    if j == 0:
      ans.append(1)
      continue
    if j == i-1:
      ans.append(1)
      continue
    else:
      ans.append(prev[j-1]+prev[j])
  print(ans)
  prev = ans