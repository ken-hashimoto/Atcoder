def hanten(n):
  n = str(n)
  n = n[::-1]
  return int(n)

def func(x):
  x1 = x
  x2 = hanten(x1)
  x3 = hanten(x2)
  return min(x1,x2,x3)

N,K = map(int,input().split())
ans = set()
cand = set()
x = K
while x <= N:
  cand.add(x)
  x *= 10
y = hanten(K)
while y <= N:
  cand.add(y)
  y *= 10

for c in cand:
  if func(c) == K:
    ans.add(c)
print(len(ans))

