import bisect
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
A_id = [[] for _ in range(2*10**5+10)]
#A_id[a] = (A[i]= aとなるようなiからなる配列)
for i in range(N):
  a = A[i]
  A_id[a].append(i)
for _ in range(Q):
  L,R,X = map(int,input().split())
  target = A_id[X]
  L -= 1
  R -= 1
  ind_L = bisect.bisect_left(target, L)
  #A_id[x]のなかでL未満のものはいくつあるか
  ind_R = bisect.bisect_right(target,R)
  #A_id[x]のなかでR以下のものはいくつあるか
  print(ind_R-ind_L)