import math
R,X,Y = map(int,input().split())
d = (X**2 + Y**2)**0.5
if R > d:
  print(2)
else:
  print(math.ceil(d/R))
