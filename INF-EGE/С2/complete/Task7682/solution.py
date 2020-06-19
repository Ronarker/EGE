a = []
n = 20
for i in range(0, n):
    a.append(int(input()))
j = 0
for i in range(n - 1):
    if (a[i] + a[i+1]) % 2 == 0 and (a[i] + a[i+1]) % 4 != 0:
        j += 1
print(j)
# Результат проверки - всё правильно