import math
N = int(input())
A = list(map(int,input().split()))
M = max(A)
A.sort()
A_set = set(A)
A_cnt = dict()
for i in range(1,2*(10**6)):
  A_cnt[i] = 0
for a in A:
  A_cnt[a] += 1

ans = 0
#A_i = A_j * A_k
for j in A_cnt.keys():
  for k in range(1,math.ceil(M/j)+10):
    i = j*k
    ans += A_cnt[j] * A_cnt[k] * A_cnt[i]
print(ans)