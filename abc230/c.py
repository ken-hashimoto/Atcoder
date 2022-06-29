N,A,B = map(int,input().split())

def is_black(i,j):
  if i-j == A-B or i+j == A+B:
    return True
  return False

P,Q,R,S = map(int,input().split())
for i in range(P,Q+1):
  ans = ""
  for j in range(R,S+1):
    if i-j == A-B or i+j == A+B:
      ans += "#"
    else:
      ans += "."
  print(ans)
