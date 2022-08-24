N = int(input())
A = list(map(int,input().split()))
#桁数の最大を求める
A.sort(reverse=True)
a1 = str(A[0])
a2 = str(A[1])
a3 = str(A[2])
ans = [
  int(a1 + a2 + a3),
  int(a1 + a3 + a2),
  int(a2 + a1 + a3),
  int(a2 + a3 + a1),
  int(a3 + a1 + a2),
  int(a3 + a2 + a1)
]
print(max(ans))

