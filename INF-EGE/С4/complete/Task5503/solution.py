# Python 3.6
N = int(input())
a14 = 0
a_max = 0
a7 = 0
a2 = 0
for i in range(N):
    a = int(input())
    if a % 14 == 0 and a > a14:
        a14 = a
    if a > a_max:
        a_max = a
    if a % 7 == 0 and a % 2 != 0:
        a7 = a
    if a % 2 == 0 and a % 7 !=  0:
        a2 = a
R = int(input())
if a14 * a_max > a7 * a2:
    R_ = a14 * a_max
else:
    R_ = a7 * a2
print('Вычисленное контрольное значение:', R_)
if R == R_:
    print('Контроль пройден')
else:
    print('Контроль не пройден')
# Решение задания Б