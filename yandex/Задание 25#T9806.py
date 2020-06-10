'''
https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=363&tag_id=19
'''
# допускается также
# использовать две
# целочисленные переменные j и k
a = []
n = 6
for i in range(0, n):
    a.append(int(input()))
j = 10000
for i in range(0, n):
    if a[i] % 6 != 0 and a[i] < j:
        j = a[i]
for i in range(0, n):
    if a[i] % 6 != 0:
        print(j)
    else:
        print(a[i])