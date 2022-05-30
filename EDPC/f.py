s = input()
t = input()
m = len(s)
n = len(t)
#dp[i][j] = (s[:i]とt[:j]の最長共通部分文字列の長さ)
#まずはdp[m][n]を求めたい
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
  for j in range(1,n+1):
    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    if s[i-1] == t[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1

#復元パート
#dpテーブルをもとに最長共通部分文字列を逆から復元する
#増えるところをななめに辿っていくイメージ
ans = 0
i = m
j = n
while i > 0 and j > 0:
  if s[i-1] == t[j-1]:
    ans = s[i-1] + ans
    i -= 1
    j -= 1
  else:
    if dp[i][j] == dp[i][j-1]:
      j -= 1
    elif dp[i][j] == dp[i-1][j]:
      i -= 1
print(ans)