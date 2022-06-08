S = int(input())
upper_flag = False
lower_flag = False
Is_distinct = False
upper = set(chr(x+65) for x in range(26))
lower = set(chr(x+97) for x in range(26))
for s in S:
  if s in upper:
    upper_flag = True
  if s in lower:
    lower_flag = True
if len(set(S)) == len(S):
  Is_distinct = True
if upper_flag and lower_flag and Is_distinct:
  print('Yes')
else:
  print('No')
