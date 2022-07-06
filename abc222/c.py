def battle(p,q):
  if p == q:
    return 'Draw'
  elif p == 'G' and q == 'P':
    return 'R'
  elif p == 'P' and q == 'C':
    return 'R'
  elif p == 'C' and q == 'G':
    return 'R'
  else:
    return 'L'
N,M = map(int,input().split())
jyanken = [list(input()) for _ in range(2*N)]
result = []
for i in range(2*N):
  result.append([0,i+1])
for i in range(M):
  for j in range(N):
    score1,name1 = result[2*j]
    score2,name2 = result[2*j+1]
    t1 = jyanken[name1-1][i]
    t2 = jyanken[name2-1][i]
    if battle(t1,t2) == 'Draw':
      continue
    elif battle(t1,t2) == 'R':
      result[2*j+1][0]+= 1
    else:
      result[2*j][0] += 1
  result.sort(key=lambda x: (-x[0], x[1]))
for item in result:
  print(item[1])
    
