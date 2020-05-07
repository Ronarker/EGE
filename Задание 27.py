'''
https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=365&tag_id=19
'''
m = 120
n = 7
a = []
b = 0
c = 0
d = 0
for i in range(n):
    a.append(int(input()))
for i in range(n - 1):
    for k in range(i + 1, n):
        if  (a[i] + a[k]) % 120 == 0:
            if (a[i] + a[k]) > b + c:
                d = a[i] + a[k]
                if i < k and a[i] > a[k]:
                    b = a[i]
                    c = a[k]
print(b, c)