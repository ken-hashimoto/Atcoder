def calc(i,j):
  return i*7 + j
N,M = map(int,input().split())
flag = True
for i in range(N):
  B = list(map(lambda x:int(x)-1,input().split()))
  if i == 0:
    s = B[0]//7
    t = B[0]%7
    for j in range(1,M):
      if (t+j)%7 == 0:
        flag = False
  for j in range(M):
    if calc(s+i,t+j) != B[j]:
      flag = False
if flag:
  print("Yes")
else:
  print("No")