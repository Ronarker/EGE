# Python 3.6
N = int(input())
X = 0  # наибольшее число, кратное 14 и являющееся произведением двух элементов последовательности

a14 = 0
a7 = 0
a2 = 0
a_max = 0
for i in range(N):
    a = int(input())
    if a % 14 == 0:
        a14 = a
    if a > a_max:
        a_max = a
    if a % 2 == 0 and a % 7 != 0 and a2 < a:
        a2 = a
    if a % 7 == 0 and a % 2 != 0 and a2 < a:
        a2 = a

X = a14 * a_max if a14 * a_max > a7 * a2 else a7 * a2
print(X)
# программа является решением задания Б