from sys import stdin

def ordem_asc(lista: list[list[int]]):
    ordenado = {}

    for pessoa, consumo in lista:
        razao = consumo // pessoa
        
        try:
            ordenado[razao] += pessoa
        except KeyError:
            ordenado[razao] = pessoa

    ordenado = [(x[1], x[0]) for x in sorted(ordenado.items())]
    return ordenado

def consumo_medio(lista: list[list[int]]):
    return sum(x[1] for x in lista) / sum(x[0] for x in lista)


cidade = 1
primeiro = True

while True:
    linha = stdin.readline().strip()
    if not linha:
        continue

    n = int(linha)
    if n == 0:
        break

    consumo_imovel = []

    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        consumo_imovel.append([x, y])

    ordenado = ordem_asc(consumo_imovel)

    if not primeiro:
        print()
    primeiro = False

    print(f"Cidade# {cidade}:")
    print(' '.join(f"{x[0]}-{x[1]}" for x in ordenado))
    print(f"Consumo medio: {f'{consumo_medio(consumo_imovel):.4f}'[:-2]} m3.")

    cidade += 1