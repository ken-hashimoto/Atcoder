N = int(input())
A = list(map(int,input().split()))
even = []
odd =[]
if N == 2 and (A[0] + A[1])%2 == 1:
  print(-1)
for a in A:
  if a%2 == 0:
    even.append(a)
  else:
    odd.append(a)
even.sort(reverse=True)
odd.sort(reverse=True)
ans = 0
if len(even) >= 2:
  ans = max(ans,even[0]+even[1])
if len(odd) >= 2:
  ans = max(ans,odd[0]+odd[1])
print(ans)
