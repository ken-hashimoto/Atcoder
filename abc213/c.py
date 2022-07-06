from copy import deepcopy

#座標圧縮をするだけなのだが解説のコードが綺麗すぎる
#https://atcoder.jp/contests/abc213/editorial/2366
H,W,N = map(int,input().split())
li = []
cnt1 = 1
cnt2 = 1
for i in range(N):
  A,B = map(int,input().split())
  li.append((A,B,i))
li_2 = deepcopy(li)
li.sort()
li_2.sort(key = lambda x:x[1])
d = dict()
for i in range(N):
  d[i] = [0,0]
for i in range(N):
  if i == 0:
      d[li[i][2]][0] = 1
      d[li_2[i][2]][1] = 1
  else:
    if li[i][0] != li[i-1][0]:
      cnt1 += 1
    if li_2[i][1] != li_2[i-1][1]:
      cnt2 += 1
    d[li[i][2]][0] = cnt1
    d[li_2[i][2]][1] = cnt2
for i in range(N):
  print(*d[i])

