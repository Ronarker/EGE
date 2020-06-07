N = int(input())
a = []
for i in range(0, N):
    a.append(int(input()))
k = 0
for i in range(0, N):
    k += a[i]
i = 0
if k % 2 == 0:
    for i in range(0, N):
        if a[i] % 2 == 0:
            i += 1
else:
    for i in range(0, N):
        if a[i] % 2 != 0:
            i += 1
print(i)