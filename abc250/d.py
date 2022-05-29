import math

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime
    
    
N = int(input())
L = 10**6 + 10
Is_prime = sieve_of_eratosthenes(L)
qqq_li = []
p_li= [0] #0を追加しておくとあとあとの処理が楽になる
for p in range(1,L+1):
  if Is_prime[p]:
    p_li.append(p)
    if p**3 < N:
      qqq_li.append(p**3)
S = len(p_li)
ans = 0
for qqq in qqq_li:
  #qqq*p <= N となるpがいくつあるかを求める
  left = 0 #leftはつねに条件をみたす
  right = S-1 #rightはつねに条件を満たさ満たさない
  q = int(qqq**(1/3))
  while left + 1 != right:
    mid = (left+right)//2
    p = p_li[mid]
    if qqq*p <= N and p < q:
      left = mid
    else:
      right = mid
  ans += left
print(ans)
  