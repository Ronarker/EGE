'''
https://ctege.info/ege-po-informatike/probnyiy-ege-2020-po-informatike-2.html
'''
# допускается также
# использовать две
# целочисленные
# переменные j, k
a = []
n = 20
for i in range(n):
    a.append(int(input()))
k = 0
for i in range(n):
    if i != n - 1:
        if (a[i] + a[i + 1]) % 6 != 0 and (a[i] * a[i + 1]) < 1000:
            k += 1
print(k)