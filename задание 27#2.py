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
    if i < 4:
        while i + z <= N - 1:
            if (a[i] * a[i + z]) % 3 == 0 and (a[i] + a[i + z]) % 3 != 0:
                m += 1
            z += 1
        z = 4
    elif i > 3:
        while i + n <= N - 1:
            if (a[i] * a[i + n]) % 3 == 0 and (a[i] + a[i + n]) % 3 != 0:
                m += 1
            n += 1
        n = 4

print(m)