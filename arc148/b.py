N = int(input())
S = input()
ans = [S]
if S == "d"*N:
  print(S)
  exit()
if S == "p":
  print("d")
  exit()
start = S.index("p")
head = S[:start]
body = ""
for i in range(start,N):
  if S[i] == "d":
    body = "p" + body
  if S[i] == "p":
    body = "d" + body
  if i+1 < N and S[i] == "p" and S[i+1] == "d":
    tmp = head + body + S[i+1:]
    ans.append(tmp)
  if i == N-1:
    tmp = head + body
    ans.append(tmp)
print(min(ans))