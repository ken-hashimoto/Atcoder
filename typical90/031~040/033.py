import math
H,W = map(int,input().split())
if H >= 2 and W >= 2:
  print(math.ceil(H/2)*math.ceil(W/2))
else:  
  print(max(H,W))