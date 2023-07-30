# 缶切りをあけるだけあける
# 最後に缶切りが必要のないものをつめていく
import bisect

N, M = map(int, input().split())
cans0 = []
cans1 = []
openers = []
result = []
for i in range(N):
    t, x = map(int, input().split())
    if t == 0:
        cans0.append(x)
    if t == 1:
        cans1.append(x)
    if t == 2:
        openers.append(x)
cans0.sort(reverse=True)
cans1.sort()
openers.sort()
# あとi個の品物が選べるとき、cans0を使って最大いくらの満足度を得られるか
X = [0] * (N + 1)
for i in range(1, N + 1):
    if i - 1 < len(cans0):
        X[i] = X[i - 1] + cans0[i - 1]
    else:
        X[i] = X[i - 1]

# あとi個の品物が選べるとき、cans1とopenerを使って最大いくらの満足度を得られるか
Y = [0] * (N + 1)
opener_cnt = 0
satisfaction = 0
left = 0
for i in range(1, N + 1):
    if opener_cnt == 0:
        if openers:
            opener_cnt += openers.pop()
    else:
        if cans1:
            opener_cnt -= 1
            satisfaction += cans1.pop()
    Y[i] = satisfaction
ans = 0
for i in range(M + 1):
    ans = max(ans, X[i] + Y[M - i])
print(ans)
