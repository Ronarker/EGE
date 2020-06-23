N = int(input())
a2 = 0
a6 = 0
a3 = 0
a1 = 0
counter = 0
for i in range(N):
    a = int(input())
    if a % 2 == 0:
        if a % 3 == 0:
            a6 += 1
        else:
            a2 += 1
    else:
        if a % 3 == 0:
            a3 += 1
        else:
            a1 += 1
print(a2 * a3 + a6 * a1 + a6 * a3)