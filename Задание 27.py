'''
https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=365&tag_id=19
'''
n = int(input())
m = 120
a = []
b = 0
c = 0
d = 0
for i in range(n):
    a.append(int(input()))
for i in range(n - 1):
    for k in range(i + 1, n):
        if  (a[i] + a[k]) % m == 0 and (a[i] + a[k]) > b + c:
            if a[i] > a[k]:
                c = a[k]
                b = a[i]
print(b, c)