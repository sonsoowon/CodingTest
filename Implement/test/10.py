"""
12-10. 자물쇠와 열쇠


"""

from operator import add

key = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

ex = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]


base = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for i in range(3):
    for j in range(3):
        base[i + 1][j] = ex[i][j]

a = [row[0:3] for row in base[1:4]]
print(a)
print([[key[i][j] for i in range(3)] for j in range(2, -1, -1)])

print([a + b for rowa, rowb in zip(key, ex) for a, b in zip(rowa, rowb)])