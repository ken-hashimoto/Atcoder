import bisect
N = int(input())
A = list(map(int,input().split()))
cum = []
res = 0
for i in range(0,N,2):
    if i == 0:
        cum.append(0)
        continue
    res += A[i] - A[i-1]
    cum.append(res)
Q = int(input())
for _ in range(Q):
    l,r = map(int,input().split())
    li = bisect.bisect(A,l)
    ri = bisect.bisect(A,r)
    ans = 0
    if li % 2 == 0:
        # 寝ている時間から始まる
        ans += A[li] - l
        li += 1
    if ri % 2 == 0:
        # 寝ている時間で終わる
        ans += r - A[ri-1]
        ri -= 1
    # 
    ans += cum[(ri-1)//2] - cum[(li-1)//2]
    print(ans)