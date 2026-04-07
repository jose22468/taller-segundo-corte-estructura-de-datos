n, w = map(int, input().split())
cambios = list(map(int, input().split()))

ruta = [0]
for x in cambios:
    ruta.append(ruta[-1] + x)

bajo = max(0, -min(ruta))
alto = min(w, w - max(ruta))

print(max(0, alto - bajo + 1))