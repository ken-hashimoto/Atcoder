def ok(i,j):
    global H,W
    return 0 <= i < H and 0 <= j < W
def toNode(i,j):
    global H,W
    return i * W + j
def getInd(s):
    global snuke
    if not s in snuke.keys():
       return  -1
    return snuke[s]
from collections import deque
H,W = map(int,input().split())
SS = []
G = [[] for _ in range(H*W)]
for i in range(H):
    S = list(input())
    SS.append(S)
dd = [(0,1),(1,0),(-1,0),(0,-1)]
snuke = {"s":0,"n":1,"u":2,"k":3,"e":4}
snuke_str = "snuke"
nodes = []
## 有向グラフを作ってbfs
for i in range(H):
    for j in range(W):
        s = SS[i][j]
        ind = getInd(s)
        if ind == -1:
            continue
        node = toNode(i,j)
        nodes.append(node)
        for d in dd:
            ni = i + d[0]
            nj = j + d[1]
            if not ok(ni,nj):
                continue
            new_s = SS[ni][nj]
            if new_s != snuke_str[(ind+1)%5]:
                continue
            nnode = toNode(ni,nj)
            G[node].append(nnode)
if len(G[0]) == 0:
    print("No")
    exit()
seen = [False for _ in range(H*W)]
d = deque()
d.append(0)
while d:
    now = d.pop()
    if seen[now]:
        continue
    seen[now] = True
    for nxt in G[now]:
        if seen[nxt]:
            continue
        d.append(nxt)
if seen[H*W-1]:
    print("Yes")
else:
    print("No")
