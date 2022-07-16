N = int(input())
M = 2*N
Q = N//4
R = N%4
if R > 0:
  x = str(R) + Q*"4"
else:
  x = Q*"4"
print(M)
print(x)