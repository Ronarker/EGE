'''
https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=363&tag_id=19
'''
# допускается также использовать две
# целочисленные переменные j и k
a = []
n = 6
for i in range(n):
    a.append(int(input()))
j = 999
k = []
for i in range(n):
    k.append(a[i] // 100)
    k.append(a[i] // 10 % 10)
    k.append(a[i] % 10)
    if k[0] == k[1] or k[0] == k[2] or k[1] == k[2]:
        if a[i] < j:
            j = a[i]
    k.clear()
for i in range(n):
    k.append(a[i] // 100)
    k.append(a[i] // 10 % 10)
    k.append(a[i] % 10)
    if k[0] == k[1] or k[0] == k[2] or k[1] == k[2]:
        print(j)
    else:
        print(a[i])
    k.clear()