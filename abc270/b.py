X,Y,Z = map(int,input().split())
if X < 0:
  X = -X
  Y = -Y
  Z = -Z
if 0 < Y < X:
  #ハンマーが必要
  if Z < Y:
    #ハンマーが入手可能なとき
    if 0 < Z:
      print(X)
      exit()
    if Z < 0:
      print(2 * abs(Z) + X)
      exit()
  else:
    print(-1)
    exit()
else:
  print(X)
  exit()