N = int(input())
done = set()
while True:
  for i in range(1,2*N+2):
    if not i in done:
      print(i,flush = True)
      done.add(i)
      break
  x = int(input())
  done.add(x)
  if x == 0:
    break