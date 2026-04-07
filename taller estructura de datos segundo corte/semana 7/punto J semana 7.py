n, m = map(int, input().split())

min_movimientos = (n + 1) // 2

resultado = -1

if n < m:
    resultado = -1
else:
    ans = min_movimientos
    while ans % m != 0:
        ans += 1
    if ans <= n:
        resultado = ans
    else:
        resultado = -1

print(resultado)