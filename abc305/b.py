p,q = input().split()
d = [3,1,4,1,5,9]
cumd = [0,3,4,8,9,14,23]
s = ["A","B","C","D","E","F","G"]
pi = s.index(p)
qi = s.index(q)
if qi < pi:
    pi,qi = qi,pi
print(s[qi-1] + s[pi])