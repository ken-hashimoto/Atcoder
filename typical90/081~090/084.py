N = int(input())
S = input()
ans = N*(N-1)//2
cnt = 0 #同じ文字が何個連続しているか
for i in range(N):
  if i == 0:
    prev = S[0]
    cnt += 1
  else:
    next = S[i]
    if prev != next: #文字が変わったら
      ans -= cnt*(cnt-1)//2 #余事象を引く
      cnt = 0
    cnt += 1
    if i == N-1:
      ans -= cnt*(cnt-1)//2
      break
    prev = next

print(ans)