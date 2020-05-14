'''
https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=365&tag_id=19
'''
m = 120
n = 7  # Вводится перед перечислением чисел т.е. n = int(input())
a = []
b = 0
c = 0
d = 0
for i in range(n):
    a.append(int(input()))
for i in range(n - 1):
    for k in range(i + 1, n):
        if (a[i] + a[k]) % 120 == 0:  # Не обрабатыется m, замени 120 на m
            if (a[i] + a[k]) > b + c:  # Эту проверку можно добавить в условие выше с помощью - and
                d = a[i] + a[k]  # Нигде не используется - лишний расход памяти
                if i < k and a[i] > a[k]:  # i < k не имеент смысла проверять так как у тебя k начинается от (i + 1)
                    b = a[i]  # По сути одно и то же число a[i] присваевается к b несколько раз, перенеси за первый цикл
                    c = a[k]
print(b, c)