N = int(input())
S = [0] + list(map(int, input().split()))

# a_{n+1} = s_{n+1} - s{n}
for i in range(N + 1):
    print(S[i + 1] - S[i])
