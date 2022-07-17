N,X,Y,Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
result = []
for i in range(N):
  result.append((i+1,A[i],B[i],A[i]+B[i]))
goukaku = [False] * (N+1)
math = sorted(result,key= lambda x:-x[1])
eng = sorted(result,key= lambda x:-x[2])
goukei = sorted(result,key= lambda x:-x[3])
ans = []
cnt_Y = 0
cnt_Z = 0
for i in range(X):
  ans.append(math[i][0])
  goukaku[math[i][0]] = True
for i in range(N):
  if cnt_Y == Y:
    break
  if goukaku[eng[i][0]] == False:
    ans.append(eng[i][0])
    goukaku[eng[i][0]] = True
    cnt_Y += 1
for i in range(N):
  if cnt_Z == Z:
    break
  if goukaku[goukei[i][0]] == False:
    ans.append(goukei[i][0])
    goukaku[goukei[i][0]] = True
    cnt_Z += 1

ans.sort()
for item in ans:
  print(item)