N = int(input())
S = set()
for i in range(1,N+1):
  User = input()
  if User in S:
    continue
  print(i)
  S.add(User)