import copy

def recursion_sterling_set(n,k):
	if k ==1:
		return [[[x for x in range(n)]]]
	elif n == k :
		return [[[x] for x in range(n)]]
	else:
		temp_n = n
		temp_k = k
		s_n_1_k_1 = recursion_sterling_set(temp_n-1,temp_k-1)
		for i in range(len(s_n_1_k_1)):
			s_n_1_k_1[i].append([temp_n-1])
		
		k_s_n_1_k= []
		temp = recursion_sterling_set(temp_n-1,temp_k)
		for i in range (k):
			temp_ = copy.deepcopy(temp)
			k_s_n_1_k += temp_
		for i in range(len(temp)*k):
			k_s_n_1_k[i][int(i/len(temp))] += [temp_n-1]
		
		return (s_n_1_k_1+k_s_n_1_k)



N,T,M = map(int,input().split())
discord = []
for i in range(M):
    a,b = map(int,input().split())
    discord.append((a,b))

ans = 0
combs = recursion_sterling_set(N,T)
for p in combs:
	l = len(p)
	ok = True
	for pp in p:
		for d in discord:
			a,b = d
			if a in pp and b in pp:
				ok = False
	if ok:
		ans += 1
print(ans)
