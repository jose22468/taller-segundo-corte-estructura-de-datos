t = int(input())

for _ in range(t):
    n = int(input())
    tiempo_libre = 1  
    resultados = []

    for _ in range(n):
        l, r = map(int, input().split())

        momento_inicio = max(tiempo_libre, l)

        if momento_inicio <= r:
            resultados.append(momento_inicio)
            tiempo_libre = momento_inicio + 1
        else:
            resultados.append(0)

    print(*(resultados))