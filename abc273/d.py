from bisect import bisect_left
from collections import defaultdict
import sys

input = sys.stdin.readline
H, W, h, w = map(int, input().split())
yoko = defaultdict(lambda: [0, W + 1])
tate = defaultdict(lambda: [0, H + 1])

N = int(input())
for _ in range(N):
    r, c = map(int, input().split())
    tate[c].append(r)
    yoko[r].append(c)
for k in tate.keys():
    tate[k].sort()
for k in yoko.keys():
    yoko[k].sort()


def dist(l, X, x, m):
    # lは入力で与えられるもの
    # Xはtate or yoko
    # xは現在地
    # mは調整につかう
    return min(l, abs(X[bisect_left(X, x) - m] - x) - 1)


Q = int(input())
for _ in range(Q):
    d, l = input().split()
    l = int(l)
    if d == "L":
        w -= dist(l, yoko[h], w, 1)
    if d == "R":
        w += dist(l, yoko[h], w, 0)
    if d == "U":
        h -= dist(l, tate[w], h, 1)
    if d == "D":
        h += dist(l, tate[w], h, 0)
    print(h, w)
