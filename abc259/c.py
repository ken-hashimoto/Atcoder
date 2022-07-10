from itertools import groupby
def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res
S = input()
T = input()

r_S = runLengthEncode(S)
r_T = runLengthEncode(T)
if len(r_S) != len(r_T):
  print("No")
  exit()
N = len(r_S)
for i in range(N):
  item_S = r_S[i]
  item_T = r_T[i]
  if item_S[0] == item_T[0] and item_S[1] == item_T[1] == 1:
    continue
  if item_S[0] == item_T[0] and item_S[1] >= 2 and item_T[1] >= 2 and item_S[1] <= item_T[1]:
    continue
  else:
    print("No")
    exit()
print("Yes")
