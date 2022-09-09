alphabet = {chr(65+i):i for i in range(26)}
mod = 998244353
def solve_even(N,S):
  dp = [0 for _ in range(N//2)]
  for i in range(N//2):
    if i == 0:
      dp[i] = alphabet[S[0]]
    else:
      dp[i] = dp[i-1]* 26 + 1 * alphabet[S[i]]
      dp[i] %= mod
  if S[N//2:] < S[:N//2][::-1]:
    print(dp[-1]%mod)
  else:
    print((dp[i] + 1)%mod)
def solve_odd(N,S):
  dp = [0 for _ in range((N+1)//2)]
  for i in range((N+1)//2):
    if i == 0:
      dp[i] = alphabet[S[0]]
    else:
      dp[i] = dp[i-1] * 26 + 1 * alphabet[S[i]]
      dp[i] %= mod
  if S[(N+1)//2:] < S[:(N-1)//2][::-1]:
    print((dp[-1])%mod)
  else:
    print((dp[-1] + 1)%mod)

def solve(N,S):
  if N%2 == 0:
    solve_even(N,S)
  if N%2 == 1:
    solve_odd(N,S)


T = int(input())
for i in range(T):
  N = int(input())
  S = input()
  solve(N,S)