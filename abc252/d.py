N = int(input())
A = list(map(int,input().split()))
d = dict()
for a in A:
  if not (a in d):
    d[a] = 0
  d[a] += 1
if len(d) < 3:
  print(0)
  exit()
keys = list(d.keys())
if len(d) == 3:
  keys = list(d.keys())
  ans = 1
  for key in keys:
    ans *= d[key]
  print(ans)
  exit()
one = sum(list(d.values())[:3])
two = d[keys[0]]*d[keys[1]] + d[keys[2]]*d[keys[1]] + d[keys[0]]*d[keys[2]]
three = d[keys[0]] * d[keys[1]] * d[keys[2]]
#one,two,threeは先頭から切り取った部分列から異なる数字をそれぞれ1,2,3個取り出すときの組み合わせの通り数
new_three,new_two,new_one = three,two,one
for i in range(3,len(d)):
  K = d[keys[i]]
  #遷移
  new_three = two*K + three
  new_two = two + one*K
  new_one = one + K
  three,two,one = new_three,new_two,new_one
print(new_three)