file = open('generator.txt')

a = []
sk1 = -1
sk2 = -1
for i in file:
    sk1 += 1
    for j in i:
        sk2 += 1
        if j == ' ':
            a.append(sk1*80 + sk2)
    sk2 = -1
e = [[] for i in range(6400)]

for i in a:
    
    if i - 80 in a:
        e[i].append(i - 80)
    if i - 1 in a:
        e[i].append(i - 1)
    if i + 1 in a:
        e[i].append(i + 1)
    if i + 7 in a:
        e[i].append(i + 80)
        

s = []
def step(x, y, k):
    s = [x]
    c = [0]
    for i in s:
        if y == s[-1]:
            break
        for j in e[i]:
            if j not in s:
                c.append(i)
                s.append(j)
            if j == y:
                break
    d = [y]
    while x != d[-1]:
        af = d[-1]
        sk = s.index(af)
        d.append(c[sk])
    d = d[::-1]
    return d

        
    
    





    

