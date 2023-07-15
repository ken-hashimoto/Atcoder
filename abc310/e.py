N = int(input())
S = input()

one_cnt = 0
zero_cnt = 0
ans = 0
for i in range(N):
    if S[i] == "0":
        one_cnt += zero_cnt
        zero_cnt = 1
    if S[i] == "1":
        zero,one = one,zero + 1
    ans += one_cnt
print(ans)
