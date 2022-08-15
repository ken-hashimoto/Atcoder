S = list(input())
N = 7
dic = {"atcoder"[i]:i+1 for i in range(7)}
for i in range(7):
  S[i] = dic[S[i]]
data = [0]*(N+1)

def add(k, x): #a_kにxを加える
    while k <= N:
        data[k] += x
        k += k & -k
 
def get(k): #a_1 + ... + a_kを求める
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s
ans = 0
for i in range(7):
  ans += i - get(S[i])
  add(S[i],1)
print(ans)