def dfs(now, d):
    global ans
    if now in d.keys():
        ans += d[now]
        return d[now]
    ret = dfs(now // 2, d) + dfs(now // 3, d)
    d[now] = ret
    return ret


N = int(input())
ans = 0
memo = dict()
memo[0] = 1
dfs(N, memo)
print(ans)
