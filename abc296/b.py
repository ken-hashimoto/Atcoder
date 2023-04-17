c1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
c2 = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == "*":
            print(c2[j] + c1[i])
            exit()
