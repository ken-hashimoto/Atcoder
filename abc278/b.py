def is_hour(h):
    return 0 <= h <= 23


def is_min(m):
    return 0 <= m <= 59


H, M = map(int, input().split())
for i in range(24):
    h = (H + i) % 24
    for j in range(60):
        m = M + j
        if m == 60:
            M = 0
            break
        trans_h = int(str(h // 10) + str(m // 10))
        trans_m = int(str(h % 10) + str(m % 10))
        if is_hour(trans_h) and is_min(trans_m):
            print(h, m)
            exit()
