import copy

def max_same(li):
  #配列liの中に存在する-1以外の整数の中でもっとも登場回数が多いモノを出力する
  tmp = 0
  num_cnt = [0 for _ in range(10**5)]
  #num_cnt[i] = (iが何回liに現れたか)
  for num in li:
    if num == -1:
      continue
    num_cnt[num] += 1
    tmp = max(tmp,num_cnt[num])
  return tmp

H,W = map(int,input().split())
Grid = [list(map(int, input().split())) for _ in range(H)]
ans = 0
prev_line = [-1 for _ in range(W)]
#Hの選び方をbit全探索する
for i in range(2**H):
  bin_i = bin(i)[2:].zfill(H)
  subgrid = []
  cnt_H = 0

  for j in range(H): #選んだ行を取り出す
    if bin_i[j] == "1":
      subgrid.append(Grid[j])
      cnt_H += 1

  for j in range(len(subgrid)):
    #ひとつずつ比較していって同じ数字が現れるところだけ残す
    #それ以外は-1で埋める
    if j == 0:
      prev_line = copy.deepcopy(subgrid[j])
    else:
      next_line = copy.deepcopy(subgrid[j])
      for k in range(W):
        if prev_line[k] != next_line[k]:
          next_line[k] = -1
      prev_line = next_line
  cnt_W = max_same(prev_line)
  ans = max(ans,cnt_H*cnt_W)
print(ans)

