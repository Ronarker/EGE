'''
https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=365&tag_id=19
'''
N = int(input())
a = []
m = 0
z = 4
for i in range(N):
    a.append(int(input()))
for i in range(N):
    while i + z <= N - 1:
        if (a[i] * a[i + z]) % 3 == 0 and (a[i] + a[i + z]) % 3 != 0:
            m += 1
        z += 1
    z = 4
print(m)