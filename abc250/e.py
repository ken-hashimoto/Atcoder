N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Q = int(input())
ans_A = [0 for _ in range(N)]
#ans_A[i] = jとすると、{A[0],...,A[i]}　⊃　{B[0],...,B[j]}
S = set()
j = 0
for i in range(N):
    S.add(A[i])
    while True:
        if j < N and B[j] in S:
            j += 1
        else:
            break
    ans_A[i] = j-1
S = set()
j = 0
ans_B = [0 for i in range(N)]
#ans_B[i] = jとすると、{B[0],...,B[i]}　⊃　{A[0],...,A[j]}
for i in range(N):
    S.add(B[i])
    while True:
        if j < N and A[j] in S:
            j += 1
        else:
            break
    ans_B[i] = j-1
for i in range(Q):
  x,y = map(int,input().split())
  x -= 1
  y -= 1
  if ans_A[x] >= y and ans_B[y] >= x:
    print("Yes")
  else:
    print("No")
