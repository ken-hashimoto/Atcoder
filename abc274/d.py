import copy
N,x,y = map(int,input().split())
A = list(map(int,input().split()))
X = []
Y = []
normalize = 10**4
for i in range(N):
  if i % 2 == 0:
    X.append((A[i],i//2))
  else:
    Y.append((A[i],(i-1)//2))
dp_x = [-1 for _ in range(2*normalize + 10)]
dp_y = [-1 for _ in range(2*normalize + 10)]
x += normalize
y += normalize
dp_new_x = [-1 for _ in range(2*normalize + 10)]
dp_new_y = [-1 for _ in range(2*normalize + 10)]
dp_x[0 + normalize] = 0
dp_y[0 + normalize] = 0
for i in range(len(X)):
  for j in range(len(dp_x)):
    if dp_x[j] == X[i][1]:
      dp_new_x[j + X[i][0]] = X[i][1] + 1
      if i== 0:
        continue
      dp_new_x[j - X[i][0]] = X[i][1] + 1
  dp_x = copy.deepcopy(dp_new_x)
for i in range(len(Y)):
  for j in range(len(dp_y)):
    if dp_y[j] == Y[i][1]:
      dp_new_y[j + Y[i][0]] = Y[i][1] + 1
      dp_new_y[j - Y[i][0]] = Y[i][1] + 1
  dp_y = copy.deepcopy(dp_new_y)
if dp_x[x] == len(X) and dp_y[y] == len(Y):
  print("Yes")
else:
  print("No")