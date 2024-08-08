import random
a = [[1 if random.randint(0, 100) <= 40 else 0 for i in range(80)] for j in range(80)]
for i in range(80):
    a[0][i] = 1
for i in range(80):
    a[79][i] = 1
for i in range(80):
    a[i][0] = 1
for i in range(80):
    a[i][79] = 1
def sk(n, m):
    k = 0
    if 0 < n < 79 and 0 < m < 79:
        if a[m][n - 1] == 1:
            k += 1
        if a[m][n + 1] == 1:
            k += 1
        if a[m + 1][n] == 1:
            k += 1
        if a[m - 1][n] == 1:
            k += 1
        if a[m - 1][n - 1] == 1:
            k += 1
        if a[m - 1][n + 1] == 1:
            k += 1
        if a[m + 1][n - 1] == 1:
            k += 1
        if a[m + 1][n + 1] == 1:
            k += 1
    return k
apstr = []
for g in range(4):
    for i in range(1, 79):
        for j in range(1, 79):
            if a[i][j] == 0:
                if sk(i, j) >= 5:
                    a[i][j] = 1
            else:
                if sk(i, j) <= 3 :
                    a[i][j] = 0
for i in range(10, 16):
    for j in range(8, 16):
        if a[i][j] == 1:
            a[i][j] = 0
for i in range(16, 26):
    for j in range(29, 26):
        if a[i][j] == 1:
            a[i][j] = 0
f = open('generator.txt', 'w')


for i in range(80):
    str1 = ''
    for j in range(80):
         if a[i][j] == 0:
            str1 += ' '
         else:
            str1 += '-'
    f.write(str1+'\n')
   
f.close()
    


















