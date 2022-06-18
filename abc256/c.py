IN = list(map(int,input().split()))
h1,h2,h3 = IN[:3]
w1,w2,w3 = IN[3:]
ans = 0
for a in range(1,30):
  for b in range(1,30):
    for c in range(1,30):
      for d in range(1,30):
        e = h1 - a - b
        f = h2 - c - d
        g = w1 - a - c
        h = w2 - b - d
        i = h3 - g - h
        if e>0 and f>0 and g>0 and h>0 and i>0 and e+f+i == w3:
          ans += 1
print(ans)