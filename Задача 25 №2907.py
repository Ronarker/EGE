N = 30
a = []
for i in range(0, N):
    a.append(int(input()))
m = 0
n = 0
for i in range(0, N):
    if a[i] % 2 == 0 and a[i] > m:
        m = a[i]
    elif a[i] % 2 != 0 and a[i] > n:
        n = a[i]
print(m - n)