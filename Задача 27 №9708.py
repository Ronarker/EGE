# Python 3.6
N = int(input())
a = []
X = 0 # наибольшее число, кратное 14 и являющееся произведением двух элементов последовательности
for i in range(N):
    a.append(int(input()))
    if len(a) > 1:
        for k in range(i):
            if a[i] * a[k] % 14 == 0 and a[i] * a[k] > X:
                X = a[i] * a[k]
print(X)
# программа является решением задания Б