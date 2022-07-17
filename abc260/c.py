N,X,Y = map(int,input().split())
if N == 1:
  print(0)
  exit()
else:
  a = 0
  b = 1
  for i in range(N-1):
    new_a = (X+1)*a + (X*Y)*b
    new_b = a + Y*b
    a = new_a
    b = new_b
  print(a)