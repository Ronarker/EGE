# Python 3.6
N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
R = 0
for i in range(N - 1):
    for k in range(i + 1, N):
        if (a[i] * a[k]) % 14 == 0 and a[i] != a[k] and (a[i] * a[k]) > R:
            for z in range(N):
                if a[i] * a[k] == a[z]:
                    R = a[z]
print(R)