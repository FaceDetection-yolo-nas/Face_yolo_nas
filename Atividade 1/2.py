def elementos_unicos(p=[], q=[]):
    l = []
    for i in range(len(p)):
        if q[i] not in p:
            l.append((q[i]))
        if p[i] not in q:
            l.append(p[i])
    print(l)


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
elementos_unicos(a, b)
