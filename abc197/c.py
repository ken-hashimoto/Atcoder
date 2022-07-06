import itertools
def calc_or(li):
  ret = 0
  for item in li:
    ret = ret | item
  return ret
N = int(input())
A = list(map(int,input().split()))
ans = []
for bits in itertools.product([0,1],repeat=N):
  tmp = []
  ans_cand = 0
  for i in range(N):
    if len(tmp) == 0:
      tmp.append(A[i])
      if i == N-1:
        if len(tmp) > 0:
          ans_cand = ans_cand ^ calc_or(tmp)
          tmp = []
      continue
    if bits[i-1] == bits[i]:
      tmp.append(A[i])
    elif bits[i-1] != bits[i]:
      ans_cand = ans_cand ^ calc_or(tmp)
      tmp = []
      tmp.append(A[i])
    if i == N-1:
      if len(tmp) > 0:
        ans_cand = ans_cand ^ calc_or(tmp)
        tmp = []
  ans.append(ans_cand)
print(min(ans))
