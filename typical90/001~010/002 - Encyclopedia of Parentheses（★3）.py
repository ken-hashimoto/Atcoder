N = int(input())
for i in range(2**N):
  bin_i = bin(i)[2:].zfill(N)
  candidate = ''
  Flag = True
  cnt = 0
  if len(bin_i) == N:
    for j in bin_i:
      if j == "0":
        candidate += '('
        cnt += 1
      else:
        candidate += ')'
        cnt -= 1
      if cnt < 0:
        Flag = False
    if cnt == 0 and Flag:
      print(candidate)
