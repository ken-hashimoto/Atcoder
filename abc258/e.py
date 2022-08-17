N, Q, X = map(int,input().split())
W = list(map(int,input().split()))
Wsum = sum(W)
loop = X//Wsum
X = X%Wsum

r = 0
s = 0
NextPotato = [-1] * N
for l in range(N):
    while s < X:
        s += W[r%N]
        r += 1
    NextPotato[l] = r % N
    s -= W[l]

inds = [-1] * N #inds[i] = (何回目にiを通るか）
route = [0] #辿ったところを記録する
now = 0
inds[now] = 0
tail = -1 #何回進んだところでループが始まるか
period = -1
while True:
    np = NextPotato[now]
    if inds[np] != -1:
        tail = inds[np] 
        period = len(route) - tail
        break
    inds[np] = len(route)
    route.append(np)
    now = np

for _ in range(Q):
    K = int(input())
    K -= 1
    if K < tail:
      ind = K
    else: #周期が始まっているならそれを考慮する
      ind = (K-tail) % period + tail
    p = route[ind] #K箱目に入れ始めるのはp番目のじゃがいも
    np = NextPotato[p] #その次にいれ始めるのはnp番目のじゃがいも
    ans = loop * N + np - p
    if p >= np and X > 0: #W_p ,... W_(N-1),W_0,...W_npという場合
        ans += N
    print(ans)
