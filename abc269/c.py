import itertools

X = int(input())
bin_X = bin(X)[2:]
num = []
for s in bin_X:
  if s == "1":
    num.append(["0","1"])
  else:
    num.append(["0"])
ans = []
for v in itertools.product(*num):
  s = "".join(v)
  ans.append(int(s,2))
ans.sort()
for a in ans:
  print(a)