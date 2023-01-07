from collections import defaultdict
def factorization(n):
    arr = defaultdict(int)
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] = cnt

    if temp!=1:
        arr[temp] = 1

    if arr==[]:
        arr[n] = 1

    return arr
def search(p,k):
    #n!がpでk回割り切れるようなもののうち最小のnを出力する
    l = 1
    r = 10**12 + 10
    while l + 1 != r:
        m = (l+r)//2
        s = 1
        cnt = 0
        while p**s <= m:
            cnt += m // p**s
            s += 1
        if cnt < k:
            l = m
        else:
            r = m
    return r

K = int(input())
pf = factorization(K)
ans_li = []
for k in pf.keys():
    ans_li.append(search(k,pf[k]))
print(max(ans_li))