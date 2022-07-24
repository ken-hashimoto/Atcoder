N = int(input())
name = set()
cnt = dict()
for i in range(N):
  S = input()
  if not S in name:
    print(S)
    name.add(S)
    cnt[S] = 1
  else:
    print(S + "(" + str(cnt[S]) + ")")
    cnt[S] += 1