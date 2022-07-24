L1,R1,L2,R2 = map(int,input().split())
li = [0]*110
for i in range(110):
  if L1 <= i <=R1-1:
    li[i] += 1
  if L2 <= i <= R2-1:
    li[i] += 1
ans = 0
for i in range(110):
  if li[i] == 2:
    ans += 1
print(ans)
