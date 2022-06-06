N = int(input())
square = [False for _ in range(N+1)]
for i in range(1,N+1):
  if i**2 > N:
    break
  square[i**2] = True
divisors = [[] for _ in range(N+1)] #divisors[i] = (iの約数)
for i in range(1,N+1):
  j = i
  while j <= N:
    divisors[j].append(i)
    j += i

#f(i) = (整数iの約数のうち最大の平方数)とする
#g(i) = i/f(i)とおく、これは整数
#i*jが平方数であることと、g(i) == g(j)は同値
#cnt[s] = (g(i) == sとなるiの個数)とすると
#もとめるのはcnt[s]**2のsum
cnt = [0 for _ in range(N+1)]
for i in range(1,N+1):
  #f(i)をもとめる
  f_i = 0
  for d in divisors[i]:
    if square[d]:
      f_i = d
  g_i = i//f_i #これがg(i)
  cnt[g_i] += 1
#cntが求まったので答えを出力
ans = 0
for s in range(1,N+1):
  ans += cnt[s]**2
print(ans)