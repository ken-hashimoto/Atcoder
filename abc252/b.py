N = int(input())
time = [[] for _ in range(10)]
#time[i] = (番号iが出現する時間のリスト)
for _ in range(N):
  S = input()
  for sec,slot_num in enumerate(S):
    time[int(slot_num)].append(sec)

ans = [0 for _ in range(10)]
#ans[i] = (番号iをそろえるのに必要な最小時間)
for slot_num in range(10):
  for sec in range(10):
    cnt = time[slot_num].count(sec)
    ans[slot_num] = max(ans[slot_num],(cnt-1)*10+sec)
print(min(ans))