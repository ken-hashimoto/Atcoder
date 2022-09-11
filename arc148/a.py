def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
N = int(input())
A = list(set(map(int,input().split())))
if len(A) == 1:
  print(1)
  exit()
A.sort()
print(A)
P = factorization(A[1]-A[0])
for prime,_ in P:
  flag = True
  r = A[0]%prime
  for i in range(N):
    if (A[i] - r)%prime != 0:
      flag = False
  if flag:
    print(1)
    exit()
print(2)