from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
init = -1
d = defaultdict(int)
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        init = query[1]
        d = defaultdict(int)
    elif query[0] == 2:
        if init == -1:
            # 一度も一番目のクエリをもらっていないとき
            A[query[1] - 1] += query[2]
        else:
            d[query[1]] += query[2]
    elif query[0] == 3:
        if init == -1:
            print(A[query[1] - 1])
        else:
            print(init + d[query[1]])
