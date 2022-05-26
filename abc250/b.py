N,A,B = map(int,input().split())
pattern_w = ''
pattern_b = ''
for i in range(N):
  if i % 2 == 0:
    pattern_w += '.' * B
    pattern_b += '#' * B
  else:
    pattern_w += '#' * B
    pattern_b += '.' * B
for i in range(N):
  if i % 2 == 0:
    for j in range(A):
      print(pattern_w)
  else:
    for j in range(A):
      print(pattern_b)
