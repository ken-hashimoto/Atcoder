N = int(input())
Poems = set()
ans_ind = 0
highest_score = 0
def Is_Original(s):
  return not (s in Poems)
for i in range(N):
  S,T = input().split()
  T = int(T)
  if Is_Original(S):
    if highest_score < T:
      ans_ind = i+1
      highest_score = T
  Poems.add(S)
print(ans_ind)