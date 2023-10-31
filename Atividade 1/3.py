def segundo_maior(l=[]):
    l.remove(max(l))
    print(max(l))


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
segundo_maior(a)
