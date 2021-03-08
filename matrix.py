def matrix_multiply(m1, m2):
    m = []
    for i in range(len(m1)):
        r = []
        for j in range(len(m2[0])):
            s = 0
            for x in range(len(m1[i])):
                s += m1[i][x] * m2[x][j]
            r.append(int(s))
        m.append(r)
    return m

def identity(n):
    m = []
    for i in range(n):
        r = []
        for j in range(n):
            if (i == j):
                r.append(1)
            else:
                r.append(0)
        m.append(r)
    return(m)

def matrix_print(m):
    for i in range(len(m)):
        for j in m[i]:
            print(str(j)),
        print("\n"),
