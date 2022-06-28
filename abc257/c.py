N = int(input())
S = input()
W = list(map(int,input().split()))
adult_cnt = 0
li = []
for i in range(N):
  li.append((W[i],S[i]))
  if S[i] == "1":
    adult_cnt += 1
li.sort(key = lambda x:x[1])
li.sort()
ans = adult_cnt
tmp = adult_cnt
for i in range(N):
  if li[i][1] == "0":
    tmp += 1
  else:
    tmp -= 1
  if i == N-1 or li[i][0] != li[i+1][0]:
    ans = max(ans,tmp)
print(ans)