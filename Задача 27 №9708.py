# Python 3.6
N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
X = 0 # наибольшее число, кратное 14 и являющееся произведением двух элементов последовательности
for i in range(N - 1): # первое число
    for k in range(i + 1, N): # второе число
        if (a[i] * a[k]) % 14 == 0 and a[i] * a[k] > X:
            X = a[i] * a[k]
print(X)