import math
N,A,B = map(int,input().split())
G = math.gcd(A,B)
L = (A*B)//G
a = N//A
b = N//B
l = N//L
def calc_sum(k):
  #1,...kまでの総和
  return k*(k+1)//2
ans = calc_sum(N) - A*calc_sum(a) - B*calc_sum(b) + L*calc_sum(l)
print(ans)
