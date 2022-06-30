N,K = map(int,input().split())
a_b = []
for _ in range(N):
  a,b = map(int,input().split())
  a_b.append([a,b])
a_b.sort()
prev_place = 0
now_money = K
for a,b in a_b:
  now_place = a
  now_money -= now_place - prev_place
  if now_money < 0:
    print(now_place + now_money)
    exit()
  now_money += b
  prev_place = a
print(a + now_money)