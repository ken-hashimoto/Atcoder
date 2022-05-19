N = int(input())
S1 = [0 for _ in range(N+1)]
S2 = [0 for _ in range(N+1)]
#S1[i] = (クラス1のi番目までの生徒の合計点数)
#S2[i] = (クラス2のi番目までの生徒の合計点数)
#LからRまでの合計点数はS[R] - S[L-1] 
for i in range(1,N+1):
  C,P = map(int,input().split())
  S1[i] = S1[i-1]
  S2[i] = S2[i-1]
  if C == 1:
    S1[i] += P
  else:
    S2[i] += P
Q = int(input())
for i in range(Q):
  L,R = map(int,input().split())
  print(S1[R] - S1[L-1],S2[R] - S2[L-1])