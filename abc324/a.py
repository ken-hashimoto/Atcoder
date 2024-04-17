N = int(input())
A = list(map(int, input().split()))
if max(A) == min(A):
    print("Yes")
else:
    print("No")
