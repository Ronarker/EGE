N = 30
a = []
for i in range(N):
    a.append(int(input()))
max_even = 0 
max_odd = 0
for i in range(N):
    if a[i] % 2 == 0 and a[i] > max_even:
        max_even = a[i]
    elif a[i] % 2 != 0 and a[i] > max_odd:
        max_odd = a[i]
print(max_even - max_odd)
# Результат проверки - всё правильно
