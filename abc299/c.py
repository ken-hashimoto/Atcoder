N = int(input())
S = input()
ans = 0
cnt = 0
for s in S:
    if s == "o":
        cnt += 1
    if s == "-":
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans) if ans != 0 else print(-1)
