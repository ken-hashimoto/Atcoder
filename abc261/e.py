N,C = map(int,input().split())
X = C
#func[0][i] = (下からi桁目の0が操作のあとどうなるか)
#func[1][i] = (下からi桁目の1が操作のあとどうなるか)
func = [
  [0] * 30,
  [1] * 30
]
for i in range(N):
  t,a = map(int,input().split())
  if t == 1:
    for j in range(30):
      func[0][j] = func[0][j] & ((a >> j) & 1)
      func[1][j] = func[1][j] & ((a >> j) & 1)
  if t == 2:
    for j in range(30):
      func[0][j] = func[0][j] | ((a >> j) & 1)
      func[1][j] = func[1][j] | ((a >> j) & 1)
  if t == 3:
    for j in range(30):
      func[0][j] = func[0][j] ^ ((a >> j) & 1)
      func[1][j] = func[1][j] ^ ((a >> j) & 1)
  ans = []
  for j in range(30):
    if (X >> j) & 1:
      ans.append(str(func[1][j]))
    else:
      ans.append(str(func[0][j]))
  tmp = ''.join(ans[::-1])
  X = int(tmp,2)
  print(X)