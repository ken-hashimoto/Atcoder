K = int(input())
m = str(K%60)
h = K//60
hh = 21 + h
if len(m) == 1:
  m = "0" + m
print(str(hh) + ":" + m)