# Python 3.6
N = int(input())
a = []
r = False
for i in range(N):
    a.append(int(input()))
R = int(input())
for i in range(N - 1):
    if r == False:
        for k in range(i + 1, N):
            if a[i] * a[k] == R: # Тебе надо заново найти R и сравнить его с введенным значением R
                r = True
                print(R)
                break
if not r: 
    print(0)
# Читай условие! Написано выведите сообщение "Вычесленное конрольное значение" и пройден контроль или нет
# Программа является решением задания А
