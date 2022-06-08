N,K = map(int,input().split())
S = []
for i in range(N):
  s = input()
  S.append(s)
ans = 0
for i in range(2**N):
  bin_i = bin(i)[2:].zfill(N)
  d = dict()
  for k in range(26):
    d[chr(k+97)] = 0
  for j in range(N):
    if bin_i[j] == '1':
      for s in S[j]:
        d[s] += 1
  ans = max(ans,list(d.values()).count(K))
print(ans)