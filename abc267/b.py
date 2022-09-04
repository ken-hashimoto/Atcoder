S = "#" + input()
r1 = [7]
r2 = [4]
r3 = [2,8]
r4 = [1,5]
r5 = [3,9]
r6 = [6]
r7 = [10]
is_standing = [True] * 7
r = [r1,r2,r3,r4,r5,r6,r7]
for i,ri in enumerate(r):
  f = False
  for p in ri:
    if S[p] == "1":
      f = True
  is_standing[i] = f

ans = True
if S[1] == "1":
  print("No")
  exit()
for i in range(7):
  if is_standing[i] == False:
    left = False
    right = False
    if True in is_standing[:i]:
      left = True
    if True in is_standing[i+1:]:
      right = True
    if left and right:
      print("Yes")
      exit()
print("No")


