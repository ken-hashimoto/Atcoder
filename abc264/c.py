from itertools import product
H1,W1 = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2,W2 = map(int,input().split())
B = [list(map(int, input().split())) for _ in range(H2)]


def op(A,hb,wb,h1,w1):
  ret = []
  for h in range(h1):
    r = []
    for w in range(w1):
      if hb[h] == 0 and wb[w] == 0:
        r.append(A[h][w])
    if len(r) > 0:
      ret.append(r)
  return ret
for hbits in product([0, 1], repeat=H1):
  for wbits in product([0, 1], repeat=W1):
    if B == op(A,hbits,wbits,H1,W1):
      print("Yes")
      exit()
print("No")