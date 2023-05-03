import heapq

N, K = map(int, input().split())
A = list(map(int, input().split()))
Q = [0]
prices = []
heapq.heapify(Q)
visited = set()
while len(prices) <= K + 1:
    p = heapq.heappop(Q)
    for i in range(N):
        if p + A[i] not in visited:
            heapq.heappush(Q, p + A[i])
            visited.add(p + A[i])
    prices.append(p)
print(prices[K])
