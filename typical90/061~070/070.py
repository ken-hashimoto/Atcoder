N = int(input())
X_li = []
Y_li = []
for i in range(N):
  X,Y = map(int,input().split())
  X_li.append(X)
  Y_li.append(Y)
X_li.sort()
Y_li.sort()
if N%2 == 0:
  ans_x = (X_li[N//2] + X_li[N//2 - 1])/2
  ans_y = (Y_li[N//2] + Y_li[N//2 - 1])/2
if N%2 == 1:
  ans_x = X_li[(N-1)//2]
  ans_y = Y_li[(N-1)//2]
ans_dist = 0
for i in range(N):
  ans_dist += abs(ans_x - X_li[i]) + abs(ans_y - X_li[i])
print(ans_dist)