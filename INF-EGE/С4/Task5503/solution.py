# Python 3.6
N = int(input())
a = []
r = 'False'
for i in range(N):
    a.append(int(input()))
R = int(input())
if R % 14 != 0:
    r = 'False'
for i in range(N - 1):
    if r == 'False':
        for k in range(i + 1, N):
            if a[i] * a[k] == R:
                r = 'True'
                print(R)
                break
if r == 'False':
    print(0)
# Программа является решением задания А
