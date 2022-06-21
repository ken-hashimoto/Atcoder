from collections import deque

def transform(moji,amari):
  if moji == 'A':
    return 'BC'[amari]
  if moji == 'B':
    return 'CA'[amari]
  if moji == 'C':
    return 'AB'[amari]

def after_op_t_times(moji,cnt):
  li = ['A', 'B', 'C']
  ind = li.index(moji)
  return li[ind + (cnt%3)]
  
S = input()
Q = int(input())
for _ in range(Q):
  t,k = map(int,input().split())
  k -= 1
  amari = deque()
  while True:
    if t == 0 or k == 0:
      break
    amari.append(k%2)
    k = k//2
    t -= 1
  if t > 0:
    now = after_op_t_times(S[0],t) #t回操作を行った後の0文字目を出力する
  else:
    now = S[k]
  while amari:
    v = amari.pop()
    now = transform(now,v)
  print(now)
