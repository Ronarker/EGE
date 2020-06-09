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
    if a[i] % 3 == 0 and a[i] < k:
        k = a[i]
for i in range(0, N):
    if k == 15000:
        print(a[i])
        continue
    elif a[i] % 2 == 0:
        print(a[i] - k)
    else:
        print(a[i])