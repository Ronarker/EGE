'''
https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=363&tag_id=19
'''
# допускается также
# использовать две
# целочисленные переменные j и k
a = []
n = 6
for i in range(n):
    a.append(int(input()))
k = -10000
for i in range(n):
    if a[i] % 2 == 0 and a[i] > k:
        k = a[i]
for i in range(n):
    if a[i] % 2 == 0:
        print(k)
    else:
        print(a[i])