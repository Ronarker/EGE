'''
https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=365&tag_id=19
'''
N = int(input())
a = []
m = 0
n = 4
z = 4
for i in range(N):
    a.append(int(input()))
for i in range(N):
    if i < N - 1:
        if i < 4:
            while i + z <= N - 1:
                if (a[i] * a[z]) % 3 == 0 and (a[i] + a[z]) % 3 != 0:
                    m += 1
                z += 1
        elif i > 3:
            for k in range(0, 4):
                if (a[i] * a[k]) % 3 == 0 and (a[i] + a[k]) % 3 != 0:
                    m += 1
            while i + n <= N - 1:
                if (a[i] * a[i + n]) % 3 == 0 and (a[i] + a[i + n]) % 3 != 0:
                    m += 1
                n += 1
    if i == N - 1:
        for k in range(0, N - 4):
            if (a[i] * a[k]) % 3 == 0 and (a[i] + a[k]) % 3 != 0:
                m += 1
print(m)