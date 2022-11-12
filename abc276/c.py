N = int(input())
P = list(map(int,input().split()))
ind = N - 1
num = [P[-1]]
while ind - 1 >= 0 and P[ind - 1] < P[ind]:
  ind -= 1
  num.append(P[ind])
e = P[ind-1]
p = P[ind]
print(e)
print(num)
for n in num:
  if n < e and p < n:
    p = n
sentou = P[:ind-1]
print(n)