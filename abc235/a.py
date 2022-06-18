def d3(x,y,z):
  return 100*x + 10 *y + z
a,b,c = map(int,list(input()))
ans = d3(a,b,c) + d3(b,c,a) + d3(c,a,b)
print(ans)