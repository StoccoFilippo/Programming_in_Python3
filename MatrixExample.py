l1 = [2, 1, 3]
l2 = [3, 1, 5]
matrix2 = []

for i in range(len(l1)):
    matrix2.append([0] * len(l1))
    for j in range(len(l2)):
        if i == j:
            matrix2[i][j] = l1[i] + l2[j]

print(matrix2)

matrix3 = []
matrix3.append(["x" * 5])
print(matrix3)
