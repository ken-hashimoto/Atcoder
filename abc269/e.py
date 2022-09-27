N = int(input())
#列をしらべる
left = 1
right = N+1
mid = (left + right - 1) // 2
while right != left + 1:
  print("?" + " "+ "1" + " " + str(N) + " "+ str(left) + " " + str(mid),flush=True)
  T = int(input())
  if T >= mid - left + 1:
    left = mid+1
    mid = (right + left - 1) // 2
  else:
    right = mid+1
    mid = (right + left - 1) // 2
retu = left
#行をしらべる
top = 1
bottom = N+1
mid = (top + bottom - 1) // 2
while bottom != top+1:
  print("?" + " "+ str(top) + " " + str(mid) + " " + "1" + " " + str(N),flush=True)
  T = int(input())
  if T >= mid - top + 1:
    top = mid+1
    mid = (bottom + top - 1) // 2
  else:
    bottom = mid+1
    mid = (bottom + top - 1) // 2
gyou = top
print("! " + str(gyou) + " " + str(retu))