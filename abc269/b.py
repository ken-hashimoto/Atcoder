G = [input() for _ in range(10)]

A_B = []
for i in range(10):
  if G[i] != "..........":
    A_B.append(i+1)

C_D = []
for i in range(10):
  flag = True
  for j in range(10):
    if G[j][i] == "#":
      flag = False
  if flag:
    C_D.append(i+1)
print(A_B)
print(C_D)