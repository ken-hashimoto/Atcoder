from collections import deque
N,M = map(int,input().split())
G = [[] for _ in range(2*10**5)]
for i in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
Q = int(input())

for i in range(Q):
    x,k = map(int,input().split())
    ans = x
    todo = deque()
    todo.append((x,0))
    seen = set()
    seen.add(x)
    while todo:
        v = todo.pop()
        node,depth = v[0],v[1]
        for new_node in G[node]:
          if depth + 1  <= k:
            todo.append((new_node,depth+1))
            if not new_node in seen:
              ans += new_node
              seen.add(new_node)
    print(ans)