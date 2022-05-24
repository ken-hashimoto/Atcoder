def keta_sum(n):
  n_str = str(n)
  tmp = 0
  for num in n_str:
    tmp += int(num)
  return tmp
N,K = map(int,input().split())
MOD = 10**5
x = N
z = 0
seen = [-1 for _ in range(10**5)]
period = 0
if K > 10**5: #Kが大きいときは周期を求める
  for i in range(K):
    y = keta_sum(x)
    z = (x+y)%MOD
    if seen[z] > 0:
      period =  i - seen[z]
      start_cnt = seen[z] + 1
      start_num = z
      break
    x = z
    seen[x] = i
  new_K = (K - start_cnt)%period
  x = start_num
  for i in range(new_K):
    y = keta_sum(x)
    z = (x+y)%MOD
    x = z
  print(x)
else: #Kが小さいときは愚直にループを回す
  for i in range(K):
    y = keta_sum(x)
    z = (x+y)%MOD
    x = z
  print(x)