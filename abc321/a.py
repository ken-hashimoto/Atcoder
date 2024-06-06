li = list(input())[::-1]
flag = True
for i in range(len(li) - 1):
    a = li[i]
    b = li[i + 1]
    if int(a) >= int(b):
        flag = False
if flag:
    print("Yes")
else:
    print("No")
