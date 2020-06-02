N = 5
a = []
for i in range(0, N):
    a.append(int(input()))
cnt = 1
for i in range(0, N - 1):
    if a[i] < a[i + 1]:
        cnt += 1
    else:
        cnt = 1
print(cnt)
