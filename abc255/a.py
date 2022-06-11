R,C = map(int,input().split())
a_1 = list(map(int,input().split()))
a_2 = list(map(int,input().split()))
if R == 1:
  print(a_1[C-1])
if R == 2:
  print(a_2[C-1])