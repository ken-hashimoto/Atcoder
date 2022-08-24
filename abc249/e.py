N,P = map(int,input().split())
dp = [[0]*(N+10) for _ in range(N+10)]
#dp[i][j] ... 圧縮前の長さがiで圧縮後の長さがjである文字列の個数
dp[0][0] = 1
for j in range(N):
    for i in range(N+1):
        if i == 0:
            c = 26
        else:
            c = 25
        for k in range(1,5):
            if j + 1 + k > N:
                continue
            if i + 10**(k-1) <= N:
                dp[i+10**(k-1)][j+1+k] += c*dp[i][j]
                dp[i+10**(k-1)][j+1+k] %= P
            if i+10**k <= N:
                dp[i+10**k][j+1+k] -= c*dp[i][j]
                dp[i+10**k][j+1+k] %= P
    for i in range(N):
        dp[i+1][j+1] += dp[i][j+1]
        dp[i+1][j+1] %= P
ans = 0
for j in range(N):
    ans += dp[N][j]
    ans %= P
print(ans)
