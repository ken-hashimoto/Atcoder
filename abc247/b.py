N = int(input())
name = []
name_cnt = dict()
for _ in range(N):
  s,t = input().split()
  name.append((s,t))
  if not s in name_cnt.keys():
    name_cnt[s] = 1
  else:
    name_cnt[s] += 1
  if s == t:
    continue
  if not t in name_cnt.keys():
    name_cnt[t] = 1
  else:
    name_cnt[t] += 1
for i in range(N):
  sei,mei = name[i]
  if name_cnt[sei] > 1 and name_cnt[mei] > 1:
    print('No')
    exit()
print('Yes')