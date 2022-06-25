N = int(input())
S = input()
W = list(map(int,input().split()))
adult_cnt = 0
for s in S:
  if s == "1":
    adult_cnt += 1
li = []
for i in range(N):
  li.append((W[i],S[i]))
li.sort(key = lambda x:x[1])
li.sort()
li_2 = [[0,0,0]]
tmp = [li[0][0],0,0]
child = 0
adult = 0
if li[0][1] == "0":
  child += 1
  tmp[1] = child
else:
  adult += 1
  tmp[2] = adult
for i in range(1,N):
  if tmp[0] != li[i][0]:
    li_2.append(tmp)
    tmp = [li[i][0],0,0]
    if li[i][1] == "0":
      child += 1
      tmp[1] = child
      tmp[2] = adult
    else:
      adult += 1
      tmp[1] = child
      tmp[2] = adult
  else:
    if li[i][1] == "0":
      child += 1
      tmp[1] = child
      tmp[2] = adult
    else:
      adult += 1
      tmp[1] = child
      tmp[2] = adult
li_2.append(tmp)
ans = 0
for item in li_2:
  ans = max(ans,item[1] + (adult_cnt - item[2]))
print(ans)