from itertools import product
N = list(input())
ans = 0
for bits in product([0, 1], repeat=len(N)):
  a = [x for bit, x in zip(bits, N) if bit == 1]
  b = [x for bit, x in zip(bits, N) if bit == 0]
  if len(a) == 0 or len(b) == 0:
    continue
  a.sort(reverse=True)
  b.sort(reverse=True)
  num1 = int(''.join(a))
  num2 = int(''.join(b))
  ans = max(ans,num1*num2)
print(ans)
