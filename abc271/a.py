N = int(input())
ans = []
base = 16
num = [str(s) for s in range(1,10)] + ["A","B","C","D","E","F"]
print(num)
for i in range(len(N)):
  amari = N%base
  N  = N//base
  ans.append(amari)
print(ans)

