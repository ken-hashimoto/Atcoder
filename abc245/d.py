import numpy as np
N,M = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))
A_Pol = np.poly1d(list(reversed(A)))
C_Pol = np.poly1d(list(reversed(C)))
B_Pol = C_Pol / A_Pol
coefB = list(map(int, B_Pol[0].c))
ans = list(reversed(coefB))
print(*ans)