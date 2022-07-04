import itertools


S,K = input().split()
K = int(K)
S = list(S)
P = list(itertools.permutations(S))
P.sort()
print(''.join(P[K-1]))
