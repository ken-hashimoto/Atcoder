N = int(input())
Coins = list(map(int,input().split()))
Coins.sort(reverse=True)
A,B,C = Coins
ans = 10**5
for i in range(10**4):
  j = 0
  while N - A*i - B*j >= 0:
    if (N - A*i - B*j)%C == 0:
      k = (N - A*i - B*j)//C
      ans = min(ans,i+j+k)
    j += 1
print(ans)