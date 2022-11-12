N = int(input())
A = list(map(int,input().split()))
two = []
three = []
res  = 0
for i in range(N):
  a = A[i]
  two_tmp = 0
  three_tmp = 0
  while a%2 == 0:
    a //= 2
    two_tmp += 1
  while a%3 == 0:
    a //= 3
    three_tmp += 1
  two.append(two_tmp)
  three.append(three_tmp)
  if i == 0:
    res = a
    continue
  if res != a:
    print(-1)
    exit()
two_m = min(two)
three_m = min(three)
two_sa = sum(two) - N*two_m
three_sa = sum(three) - N*three_m
print(two_sa + three_sa)