cards = list(map(int,input().split()))
cards.sort()
if cards[0] == cards[1] == cards[2] and cards[2] != cards[3] and cards[3]  == cards[4]:
  print("Yes")
  exit()
if cards[0] == cards[1] and cards[1] != cards[2] and cards[2] == cards[3]  == cards[4]:
  print("Yes")
  exit()
print("No")