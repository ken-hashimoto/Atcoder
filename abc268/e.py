N = int(input())
P = list(map(int,input().split()))
d = {P[i]:i for i in range(N)}
dis = []
sage_diff = 0
age_diff = 0
limit = [[] for i in range(N)]
if N % 2 == 0:
  for i in range(N):
    man = i
    t = N//2
    if (d[i] - i)%N == t:
      limit[0].append((man,"age"))
      limit[N//2].append((man,"sage"))
      age_diff += 1
      dis.append((d[i] - i)%N)
    if (d[i] - i)%N > t:
      limit[(i-d[i])%N].append((man,"sage"))
      limit[((i-d[i])%N + N//2)%N].append((man,"age"))
      sage_diff += 1
      dis.append((i-d[i])%N)
    if 0 < (d[i]-i)%N < t:
      r = t - (d[i]-i)%N
      limit[r%N].append((man,"age"))
      limit[(r%N + t)%N].append((man,"sage"))
      age_diff += 1
      dis.append((d[i]-i)%N)
    if (d[i]-i)%N == 0:
      sage_diff += 1
      limit[0].append((max,"sage"))
      limit[N//2].append((max,"age"))
      dis.append(0)
  ans = sum(dis)
  tmp = ans
  for i in range(N):
    members = limit[i]
    for member,cond in members:
      if cond == "sage":
        sage_diff -= 1
        age_diff += 1
      if cond == "age":
        age_diff -= 1
        sage_diff += 1
    tmp = tmp - sage_diff + age_diff
    ans = min(tmp,ans)

  print(ans)
if N % 2 == 1:
  wait = 0
  t = (N-1)//2
  for i in range(N):
    man = i
    if (d[i] - i)%N == t:
      age_diff += 1
      limit[0].append((man,"wait"))
      limit[(t+1)%N].append((man,"sage"))
      dis.append((d[i] - i)%N)
      continue
    if (d[i] - i)%N > t:
      sage_diff += 1
      limit[(i-d[i])%N].append((man,"sage"))
      limit[((i-d[i])%N + t)%N].append((man,"wait"))
      dis.append((i - d[i])%N)
      continue
    if 0 < (d[i] - i)%N < t:
      age_diff += 1
      r = t - (d[i] - i)%N
      limit[r%N].append((man,"wait"))
      limit[(r%N + t+1)%N].append((man,"sage"))
      dis.append((d[i]-i)%N)
    if (d[i] - i)%N == 0:
      sage_diff += 1
      limit[t%N].append((man,"wait"))
      limit[(t%N + t+1)%N].append((man,"sage"))
      dis.append(0)
  ans = sum(dis)
  tmp = ans
  for i in range(N-1):
    members = limit[i]
    sage_diff += wait
    wait = 0
    for member,cond in members:
      if cond == "sage":
        sage_diff -= 1
        age_diff += 1
      if cond == "wait":
        wait += 1
        age_diff -= 1 
    tmp = tmp - sage_diff + age_diff
    ans = min(tmp,ans)
  print(ans)