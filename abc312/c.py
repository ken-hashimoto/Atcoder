import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
## 二分探索
A.sort()
B.sort()
ng = -1
ok = 10**9 + 10
while ng + 1 != ok:
    mid = (ng + ok) // 2
    kaite = bisect.bisect_right(A, mid)
    urite = M - bisect.bisect_left(B, mid)
    if kaite >= urite:
        ok = mid
    else:
        ng = mid
print(ok)
