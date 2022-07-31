Y = int(input())
if Y % 4 == 2:
  print(Y)
  exit()
else:
  while Y % 4 != 2:
    Y += 1
  print(Y)
  exit()