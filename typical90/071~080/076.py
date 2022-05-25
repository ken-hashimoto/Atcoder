N = int(input())
A = list(map(int,input().split()))
whole_size = sum(A)
if whole_size%10 != 0:
  print("No")
  exit()
A = A + A
limit = whole_size//10
#しゃくとり法
left = 0
size = 0
for right in range(2*N):
  if size > limit:
    while size > limit:
      size -= A[left]
      left += 1
      if left == 2*N:
        break
  if size < limit:
    size += A[right]
    continue
  if size == limit:
    print("Yes")
    exit()
print('No')
