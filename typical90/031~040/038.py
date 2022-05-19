import math
A,B = map(int,input().split())
G = math.gcd(A,B)
L = A*B//G
if L > 10**18:
  print('Large')
else:
  print(L)