N,K = map(int,input().split())
A = list(map(int,input().split()))
result = ['Second' for _ in range(10**5 + 1)]
for i in range(10**5 + 1):
  for a in A:
    if i - a >= 0:
      #もしi個山の中からa個の石をとりさったとき、それをスタートと思うと後手が勝つということなのでi個の場合は先手が勝つ
      if result[i-a] == 'Second':
        result[i] = 'First'
        break
print(result[K])