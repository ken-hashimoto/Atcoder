N,M = map(int,input().split())
functions = []
for i in range(N):
    p,c,*fs = map(int,input().split())
    functions.append([p,c,set(fs)])
    
for i in range(N):
    for j in range(N):
        fi = functions[i]
        fj = functions[j]
        if fi[0] >= fj[0] and fj[2] >= fi[2]:
            if fi[0] > fj[0] or fj[2] > fi[2]:
                print("Yes")
                exit()
print("No")

