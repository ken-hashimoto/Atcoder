import math
T = int(input())
L,X,Y = map(int,input().split())
Q = int(input())
pi = math.pi
for i in range(Q):
  E = int(input())
  phi = (2*pi*E)/T
  y = -L/2 * math.cos(phi - pi/2)
  z = L/2 * math.sin(phi - pi/2) + L/2
  d = ((X**2 + (Y-y)**2))**0.5
  ans = math.degrees(math.atan2(z, d))
  print(ans)