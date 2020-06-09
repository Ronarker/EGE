'''
https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=363&tag_id=19
'''
# кроме уже указанных
# допускается использование
# целочисленных переменных
# k, m
a = []
N = 5
for i in range(0, N):
    a.append(int(input()))
k = 15000
for i in range(0, N):
    if a[i] < k:
        k = a[i]
k = k * 2
for i in range(0, N):
    if a[i] < k:
        a[i] = a[i] * 2
        print(a[i])
    else:
        print(a[i])