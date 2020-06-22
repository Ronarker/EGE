A = []
N = 10
for i in range(N):
    row = []
    for k in range(N):
        row.append(int(input()))
    A.append(row)
row_sum = 0
is_magic_cube = True
for i in range(N):
    row_sum += A[0][i]
for i in range(1, N):
    if row_sum != sum(A[i]):
        is_magic_cube = False
        break
if is_magic_cube:
    col_sum = sum(A[:][0])
    for i in range(1, N):
        if col_sum != sum(A[:][i]):
            is_magic_cube = False
            break
if is_magic_cube:
    sum1 = 0
    sum2 = 0
    for i in range(N):
        sum1 += A[i][i]
        sum2 += A[i][N - i - 1]
    is_magic_cube = sum1 == sum2
if is_magic_cube:
    print('является магическим квадратом')
else:
    print('не является магическим квадратом')