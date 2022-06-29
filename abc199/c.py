def change(x):
  if x < N:
    return x + N
  if x >= N:
    return x - N
N = int(input())
S = list(input())
Q = int(input())
hanten_cnt = 0
for _ in range(Q):
  t,a,b = map(int,input().split())
  a -= 1
  b -= 1
  if t == 1:
    if hanten_cnt%2 == 0:
      S[a],S[b] = S[b],S[a]
    else:
      a = change(a)
      b = change(b)
      S[a],S[b] = S[b],S[a]
  else:
    hanten_cnt += 1

if hanten_cnt%2 == 0:
  print(''.join(S))
else:
  print(''.join(S[N:]) + ''.join(S[:N]))