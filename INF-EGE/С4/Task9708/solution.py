# Python 3.6
N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
X = 0 # наибольшее число, кратное 14 и являющееся произведением двух элементов последовательности
for i in range(N):
    k = N - 1
    if a[i] != a[k - i]:
        if (a[i] * a[k - i]) % 14 == 0 and a[i] * a[k - i] > X:
            X = a[i] * a[k - i]
print(X)
# программа является решением задания Б
