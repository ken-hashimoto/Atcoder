def isKaibun(s):
    isKaibun = True
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            isKaibun = False
    return isKaibun


S = input()
ans = 0
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        if isKaibun(S[i:j]):
            ans = max(ans, j - i)
print(ans)
