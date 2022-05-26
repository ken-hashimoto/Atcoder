N,Q = map(int,input().split())
li = list(range(1,N+1))
order = dict()
#order[i] = (iがリストの何番目にあるか、つまりli[order[i]] = i)
for i in range(1,N+1):
  order[i] = i-1
for i in range(Q):
  x = int(input())
  x_ind = order[x]
  if x_ind == N-1: #xが右端にあるとき
    y = li[x_ind-1]
    li[x_ind],li[x_ind-1] = li[x_ind-1],li[x_ind]
    order[y] = x_ind
    order[x] = x_ind-1
  else:
    y = li[x_ind+1]
    li[x_ind],li[x_ind+1] = li[x_ind+1],li[x_ind]
    order[y] = x_ind
    order[x] = x_ind+1
for num in li:
  print(num)
