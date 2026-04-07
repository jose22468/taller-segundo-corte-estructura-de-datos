n = int(input())
monedas = list(map(int, input().split()))

monedas.sort(reverse=True)

suma_total = sum(monedas)

mi_suma = 0
cantidad_monedas = 0

for moneda in monedas:
    mi_suma += moneda
    cantidad_monedas += 1
    
    if mi_suma > (suma_total - mi_suma):
        break

print(cantidad_monedas)