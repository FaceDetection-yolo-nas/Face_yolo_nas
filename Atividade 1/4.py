def nomes_alfabético(l=[(), ()]):
    k = sorted(l, key=lambda pessoas: pessoas[0])
    print(k)


a = [("Bernado", 30), ("Caio", 10), ("Ana", 20)]
nomes_alfabético(a)
