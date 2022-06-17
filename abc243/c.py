N = int(input())
x_y = []
for i in range(N):
  X,Y = map(int,input().split())
  x_y.append([X,Y,i])
S = input()
for i in range(N):
  ind = x_y[i][2]
  x_y[i][2] = S[ind]
x_y.sort() #x座標でソート
x_y.sort(key=lambda x:x[1]) #Y座標でソート
for i in range(1,N):
  x,y,s = x_y[i-1]
  nx,ny,ns = x_y[i]
  #ソートしたことでnx > xが常に成立する
  if y == ny and s == 'R' and ns == 'L':
    print('Yes')
    exit()

print('No')

  