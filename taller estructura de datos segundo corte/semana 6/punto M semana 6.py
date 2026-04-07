import sys
from bisect import bisect_left

def resolver():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    secuencia = map(int, input_data[1:])
    
    lista_ordenada = []
    profundidades = [0] * (n + 2)
    
    profundidades[0] = -1
    profundidades[n + 1] = -1
    
    c = 0 
    
    for x in secuencia:
        idx = bisect_left(lista_ordenada, x)
        
        izq = lista_ordenada[idx - 1] if idx > 0 else 0
        der = lista_ordenada[idx] if idx < len(lista_ordenada) else n + 1
        
        prof_x = max(profundidades[izq], profundidades[der]) + 1
        profundidades[x] = prof_x
        
        lista_ordenada.insert(idx, x)
        
        c += prof_x
        print(c)

if __name__ == "__main__":
    resolver()