from math import atan2, pi

# Ray casting algorithm
def inside_polygon(p0, qs):
    cnt = 0
    L = len(qs)
    x, y = p0
    for i in range(L):
        x0, y0 = qs[i-1]; x1, y1 = qs[i]
        x0 -= x; y0 -= y
        x1 -= x; y1 -= y

        cv = x0*x1 + y0*y1
        sv = x0*y1 - x1*y0
        if sv == 0 and cv <= 0:
            # a point is on a segment
            return True

        if not y0 < y1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        if y0 <= 0 < y1 and x0*(y1 - y0) > y0*(x1 - x0):
            cnt += 1
    return (cnt % 2 == 1)
def line_cross_point(P0, P1, Q0, Q1):
    x0, y0 = P0; x1, y1 = P1
    x2, y2 = Q0; x3, y3 = Q1
    a0 = x1 - x0; b0 = y1 - y0
    a2 = x3 - x2; b2 = y3 - y2

    d = a0*b2 - a2*b0
    if d == 0:
        # two lines are parallel
        return None

    # s = sn/d
    sn = b2 * (x2-x0) - a2 * (y2-y0)
    # t = tn/d
    #tn = b0 * (x2-x0) - a0 * (y2-y0)
    return x0 + a0*sn/d, y0 + b0*sn/d
ax,ay = map(int,input().split())
bx,by = map(int,input().split())
cx,cy = map(int,input().split())
dx,dy = map(int,input().split())
A = (ax,ay)
B = (bx,by)
C = (cx,cy)
D = (dx,dy)
qs = [A,B,C,D]
x,y = line_cross_point(A,C,B,D)
P = (x,y)
if inside_polygon(P, qs):
  print("Yes")
else:
  print("No")