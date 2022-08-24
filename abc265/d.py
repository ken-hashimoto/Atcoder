import itertools

def judge(cum,l,r,P,Q,R):
  #[cum[l], ... ,cum[r-1]]で考える
  ok = l
  ng = r+1
  while ok + 1 != ng:
    m = (ok+ng)//2
    if cum[m] - cum[l] <= P:
      ok = m
    else:
      ng = m
  if cum[ok] - cum[l] != P:
    return False
  left = ok
  ok = r
  ng = l-1
  while ng + 1 != ok:
    m = (ng+ok)//2
    if cum[m] - cum[r] >= -R:
      ok = m
    else:
      ng = m
  if cum[ok] - cum[r] != -R:
    return False
  right = ok
  if cum[right] - cum[left] != Q:
    return False
  return True
N,P,Q,R = map(int,input().split())
A = list(map(int,input().split()))
cum = [0] + list(itertools.accumulate(A))
# cum[i] = A[0] + ... + A[i-1]
# A[l] + ... + A[r-1] = cum[r] - cum[l]
r = 0
s = 0
for l in range(N+1):
  while r < l:
    r += 1
  while cum[r] - cum[l] < P+Q+R and r+1 <= N:
    r += 1
  if cum[r] - cum[l] == P+Q+R:
    if judge(cum,l,r,P,Q,R):
      print("Yes")
      exit()

print("No")