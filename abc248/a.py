S = input()
d = dict()
for i in range(10):
  d[i] = 0
for s in S:
  s = int(s)
  d[s] = 1
for key in d.keys():
  if d[key] == 0:
    print(key)
    exit()