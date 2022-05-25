N,Q = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
margin = [] #階差数列
for i in range(N):
  if i == 0:
    continue
  else:
    margin.append(A[i]-A[i-1])
    ans += abs(A[i]-A[i-1]) #初期状態の不便さ
for  i in range(Q):
  L,R,V = map(int,input().split())
  L -= 1
  R -= 1
  before = 0
  after = 0
  #地殻変動する両端が前後でどう変わるかを見る
  if 0 <= L-1 < N-1:
    before += abs(margin[L-1])
    margin[L-1] += V
    after += abs(margin[L-1])
  if 0 <= R < N-1:
    before += abs(margin[R])
    margin[R] -= V
    after += abs(margin[R])
  ans += after - before
  print(ans)
