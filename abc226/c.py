from collections import deque


N = int(input())
INPUT = []
for _ in range(N):
  tmp = list(map(int,input().split()))
  T,K,A = tmp[0],tmp[1],tmp[2:]
  INPUT.append([T,K,A])
time = INPUT[N-1][0]
todo = deque(INPUT[N-1][2])
acquired_trick = [False for _ in range(N)]
while todo:
  v = todo.pop()
  #技vを習得していなければ習得し、習得していればスルーする
  if acquired_trick[v-1]:
    continue
  time += INPUT[v-1][0]
  todo.extend(INPUT[v-1][2])
  acquired_trick[v-1] = True
print(time)

