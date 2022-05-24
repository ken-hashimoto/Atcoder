N,P,Q = map(int,input().split())
A = list(map(lambda x:int(x)%P,input().split()))
ans = 0
for i in range(N):
  tmp1 = A[i]%P
  for j in range(i+1,N):
    tmp2 = tmp1*A[j]%P
    for k in range(j+1,N):
      tmp3 = tmp2*A[k]%P
      for l in range(k+1,N):
        tmp4 = tmp3*A[l]%P
        for m in range(l+1,N):
          tmp5 = tmp4*A[m]%P
          if (tmp5 - Q)%P == 0:
            ans += 1
print(ans)
