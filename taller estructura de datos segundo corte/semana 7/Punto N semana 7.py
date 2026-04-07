entrada = list(map(int, input().split()))
posiciones = sorted(entrada[:3])
d = entrada[3]

p1, p2, p3 = posiciones

movimiento_izq = max(0, d - (p2 - p1))

movimiento_der = max(0, d - (p3 - p2))

print(movimiento_izq + movimiento_der)
