def B_op_to_right(i,j,li):
  now = i
  while now != j:
    li.append("B " + str(now+1))
    now += 2
def B_op_to_left(i,j,li):
  now = j
  while now != i:
    now -= 2
    li.append("B " + str(now+1))

N = int(input())
P = list(map(int,input().split()))
ans = []
#d[num] = numがPの中で何番目にいるか（0-indexed）
for i in range(N):
  if i%2 == 0:
    if P[i]%2 == 0:
      flag = True
      for j in range(i,N):
        if j%2 == 0 and P[j]%2 == 1:
          flag = False
          P[i],P[j] = P[j],P[i]
          B_op_to_right(i,j,ans)
          B_op_to_left(i,j-2,ans)
          break
      if i+1 < N and P[i+1]%2 == 1 and flag:
          P[i],P[i+1] = P[i+1],P[i]
          ans.append("A " + str(i+1))
    continue
  if i%2 == 1:
    if P[i]%2 == 1:
      flag = True
      for j in range(i,N):
        if j%2 == 1 and P[j]%2 == 0:
          flag = False
          P[i],P[j] = P[j],P[i]
          B_op_to_right(i,j,ans)
          B_op_to_left(i,j-2,ans)
          break
      if i+1 <N and P[i+1]%2 == 0 and flag:
        P[i],P[i+1] = P[i+1],P[i]
        ans.append("A " + str(i+1))
d = {P[i]:i for i in range(N)}
for i in range(1,N+1):
  if d[i] == i-1: #もう操作のしようがないなら何もしなくてよい
    continue
  while d[i] > i:
    nxt = P[d[i]-2]
    ans.append("B " + str(d[i]-2 + 1))
    P[d[i]],P[d[i]-2] = P[d[i]-2],P[d[i]]
    d[nxt] += 2
    d[i] -= 2
  if d[i] == i:
    nxt = P[d[i]-1]
    ans.append("A " + str(d[i]-1 + 1))
    P[d[i]],P[d[i]-1] = P[d[i]-1],P[d[i]]
    d[nxt] += 1
    d[i] -= 1
print(len(ans))
for a in ans:
  print(a)