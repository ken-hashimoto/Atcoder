import collections
N = int(input())
A = list(map(lambda x: int(x)%46,input().split()))
B = list(map(lambda x: int(x)%46,input().split()))
C = list(map(lambda x: int(x)%46,input().split()))
A_cnt = collections.Counter(A)
B_cnt = collections.Counter(B)
C_cnt = collections.Counter(C)
ans = 0
for i in range(46):
  for j in range(46):
    for k in range(46):
      if (i+j+k)%46 == 0:
        ans += A_cnt[i]*B_cnt[j]*C_cnt[k]
print(ans)