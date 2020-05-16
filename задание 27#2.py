'''
https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=365&tag_id=19
'''
N = int(input())
a = []
m = 0
for i in range(N):
    a.append(int(input()))
for i in range(N):
    for j in range(i + 4, N):
        if (a[i] * a[j]) % 3 == 0 and (a[i] + a[j]) % 3 != 0:
            m += 1
print(m)