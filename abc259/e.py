from collections import defaultdict
N = int(input())
nums = []
cnt = defaultdict(int)
d = defaultdict(int)
for i in range(N):
    num = []
    m = int(input())
    for j in range(m):
      p,e = map(int,input().split())
      num.append((p,e))
      d[p] = max(d[p],e)
    nums.append(num)
for i in range(N):
    num = nums[i]
    for j in range(len(num)):
        p,e = num[j][0],num[j][1]
        if d[p] == e:
            cnt[p] += 1
ans = 0
whole_lcm = True
for i in range(N):
    num = nums[i]
    flag = False
    for j in range(len(num)):
        p,e = num[j][0],num[j][1]
        if cnt[p] == 1 and e == d[p]:
            flag = True
    if flag:
        ans += 1
    if not flag and whole_lcm:
      ans += 1
      whole_lcm = False

print(ans)
