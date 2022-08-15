N,M = map(int,input().split())
A = list(map(int,input().split()))
ok = [True]*(M+1)
#ok[i] = Trueはiが問題の条件を満たすことを意味する
div = set() #Aに現れる素因数を格納
def make_divisors(n):
    i = 1
    while i*i <= n:
        if n % i == 0:
            div.add(i)
            if i != n // i:
                div.add(n//i)
        i += 1
    return
for a in A:
  make_divisors(a)
div = list(div)
for d in div:
  if d == 1:
    continue
  k = 1
  while k*d < M+1:
    ok[k*d] = False
    k += 1
ans = []
for i in range(1,M+1):
  if ok[i]:
    ans.append(i)
print(len(ans))
for a in ans:
  print(a)
