def acha_primos(l=[]):
    p = []
    for i in range(1, len(l)):
        k = 0
        for j in range(2, len(l)):
            if l[i] % j == 0 and l[i] != j:
                k += 1
        if k == 0:
            p.append(l[i])
    print(p)


g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
acha_primos(g)
