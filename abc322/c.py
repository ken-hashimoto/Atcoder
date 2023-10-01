import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    day = i + 1
    ind = bisect.bisect_left(day)
    print(A[ind] - day)
