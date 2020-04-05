'''
https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=363&tag_id=19
'''
# допускается также использовать две
# целочисленные переменные j и k
# k - минимум
a = []
n = 30
for i in range(0, n):
    a.append(int(input()))
k = 10000
for i in range(0, n):
    if int(a[i]) % 6 != 0:
        if int(a[i]) < k:
            k = int(a[i])
for i in range(0, n):
    if int(a[i]) % 6 != 0:
        a.insert(i, k)
        a.remove(int(a[i + 1]))
    print(int(a[i]))

