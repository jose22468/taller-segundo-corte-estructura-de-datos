import math

def resolver():
    t_str = input()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        k = int(input())
        
        inicio = 1
        fin = 2 * 10**18 
        resultado = fin
        
        while inicio <= fin:
            medio = (inicio + fin) // 2
            
            encendidas = medio - math.isqrt(medio)
            
            if encendidas >= k:
                resultado = medio
                fin = medio - 1
            else:
                inicio = medio + 1
        
        print(resultado)

if __name__ == "__main__":
    resolver()