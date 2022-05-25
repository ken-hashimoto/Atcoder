def range_sum(l,r):
  #l,l+1,...,r-1,rの和を出力
  return (r-l+1)*(r+l)//2
L,R = map(int,input().split())
keta_L = len(str(L))
keta_R = len(str(R))
MOD = 10**9 + 7
#L以上の数であって桁数がLと同じモノはL,...,10**keta_L -1
#R以下の数であって桁数がRと同じモノは10**(keta_R-1),...,R
ans = 0
if keta_L == keta_R:
  ans = range_sum(L,R)*keta_L #これはL,L+1,...R-1,Rの和
  ans %= MOD
  print(ans)
  exit()
else:
  for keta in range(keta_L,keta_R+1):
    if keta == keta_L:
        ans += range_sum(L,10**keta_L-1)*keta_L
        ans %= MOD
        continue
    if keta == keta_R:
        ans += range_sum(10**(keta_R-1),R)*keta_R
        ans %= MOD
        continue
    else:
      ans += range_sum(10**(keta-1),10**keta-1)*keta
      ans %= MOD
  print(ans)