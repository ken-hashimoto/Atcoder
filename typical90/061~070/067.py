def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])
N_8,K = input().split()
K = int(K)
if N_8 == '0':
  print(0)
  exit()
for _ in range(K):
  N_10 = int(N_8,8)
  N_9 = str(base_n(N_10, 9))
  N_9_li = list(N_9)
  for i in range(len(N_9_li)):
    if N_9_li[i] == '8':
      N_9_li[i] = '5'
  N_8 = ''.join(N_9_li)
print(N_8)