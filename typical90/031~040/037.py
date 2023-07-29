class SegTree:
    def __init__(self, n, op, id):
        self.size = 2 ** (n - 1).bit_length()
        self.id = id
        self.data = [id] * (self.size * 2)
        self.op = op

    def init(self, A):
        N = len(A)
        for i in range(N):
            self.data[self.size + i] = A[i]
        for i in range(self.size - 1, 0, -1):
            self.data[i] = self.op(self.data[2 * i], self.data[2 * i + 1])

    def update(self, k, x):
        data = self.data
        k += self.size
        data[k] = x
        while k > 0:
            k = k // 2
            data[k] = self.op(data[2 * k], data[2 * k + 1])

    def query(self, l, r):
        data = self.data
        l += self.size
        r += self.size
        l_res, r_res = self.id, self.id
        while l < r:
            if l % 2 == 1:
                l_res = self.op(l_res, data[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                r_res = self.op(r_res, data[r])
            l = l // 2
            r = r // 2

        res = self.op(l_res, r_res)
        return res

    def point_get(self, i):
        i += self.size
        return self.data[i]


W, N = map(int, input().split())

ide_ele = -1
s = SegTree(W + 1, max, ide_ele)
s.update(0, 0)
for i in range(N):
    L, R, V = map(int, input().split())
    for j in range(W, -1, -1):
        now = s.point_get(j)
        x = s.query(max(j - R, 0), j - L + 1)
        if x == -1:
            continue
        if now < x + V:
            s.update(j, x + V)
print(s.point_get(W))
