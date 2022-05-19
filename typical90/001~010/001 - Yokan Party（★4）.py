#入力
N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))

def solve(M):
    now = 0
    prev = 0
    cut = 0
    #それぞれのピースの長さがM以上となるように切り分ける
    for i in range(N):
        now = A[i]
        if now - prev >= M and L - now >= M:
            cut += 1
            prev = now
    if cut >= K:
        #切り分けた回数がK以上なら答えはM未満になり得ない
        #つまり答えはM以上
        return True
    else:
        return False

#left <= 答え < right
left = -1
right = L+1
while left + 1 != right:
    mid = (left + right)//2
    if solve(mid):
        left = mid
    else:
        right = mid
print(left)