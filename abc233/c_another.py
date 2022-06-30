import math
import itertools
N,X = map(int,input().split())
A = [list(map(int, input().split()))[1:] for _ in range(N)]
ans = 0
for v in itertools.product(*A):
  if math.prod(v) == X:
    ans += 1
print(ans)