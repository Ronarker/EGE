'''
https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=363&tag_id=19
'''
# кроме уже указанных
# допускается использование
# целочисленных переменных
# k, m
a = []
N = 2018
k = 15000
for i in range(0, N):
    a.append(int(input()))
for i in range(0, N):
    if int(a[i]) < k:
        k = int(a[i])
k = k * 2
for i in range(0, N):
    if int(a[i]) > k:
        print(a[i] - k)
    else:
        print(a[i])