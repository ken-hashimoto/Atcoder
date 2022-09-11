import itertools

def dfs(names,used,now,nokori,ng,required):
  # names ... 並び替えた名前のリスト
  # used ... namesのうちいくつを使ったか
  # now ... いまできている文字列
  # nokori  ... あと何回アンダーバーを使えるか
  # required ... 0のときは名前をいれる必要がある,1のときはアンダーバーを入れる必要がある,2のときはどちらをいれてもよい
  
  if used == N:
    if not now in ng:
      print(now)
      exit()
    return
  if required == 0:
    dfs(names,used + 1,now+names[used],nokori,ng,1)
    return
  if required == 1:
    dfs(names,used,now+"_",nokori,ng,2)
    return
  if required == 2 and nokori == 0:
    dfs(names,used,now,nokori,ng,0)
  if required == 2 and nokori >= 1:
    dfs(names,used+1,now+names[used],nokori,ng,1)
    dfs(names,used,now+"_",nokori-1,ng,2)
N,M = map(int,input().split())
names = []
len_s = 0
for i in range(N):
  S = input()
  len_s += len(S)
  names.append(S)
ng = set()
for i in range(M):
  T = input()
  ng.add(T)
amari = 16 - len_s - (N-1)
if N == 1:
  if S in ng or len(S) < 3:
    print(-1)
    exit()
  else:
    print(S)
    exit()
for v in list(itertools.permutations(names,N)):
  dfs(v,0,"",amari,ng,0)

print(-1)
