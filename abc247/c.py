N = int(input())

def S_n(n):
  if n == 1:
    return [1]
  s = S_n(n-1)
  return s + [n] + s

print(*(S_n(N)))
