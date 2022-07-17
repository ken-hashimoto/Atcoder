S = input()
d = {s:0 for s in set(S)}
for s in S:
  d[s] += 1
for key in d.keys():
  if d[key] == 1:
    print(key)
    exit()
print(-1)
