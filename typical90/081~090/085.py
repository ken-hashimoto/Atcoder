def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
K =int(input())
ans = 0
divisors = make_divisors(K)[::-1]
L = len(divisors)
S = set()
for a in divisors:
  bc = K//a
  if a*a < bc:
    break
  tmp = 0
  for i in range(divisors.index(bc),L):
    if bc%divisors[i] == 0:
      b = divisors[i]
      c = bc//divisors[i]
      if c <= b <= a:
        S.add((a,b,c))
print(len(S))
