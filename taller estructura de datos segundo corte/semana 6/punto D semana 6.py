import sys

def resolver():
    datos = sys.stdin.read().split()
    if not datos:
        return
    
    idx = 0
    t = int(datos[idx])
    idx += 1
    
    resultados = []
    
    for _ in range(t):
        n = int(datos[idx])
        k = int(datos[idx+1])
        idx += 2

        posiciones = []
        for _ in range(k):
            posiciones.append(int(datos[idx]))
            idx += 1
        posiciones.sort(reverse=True)
        
        pasos_del_gato = 0
        ratones_salvados = 0
        
        for p in posiciones:
            if p > pasos_del_gato:
                distancia_al_agujero = n - p
                pasos_del_gato += distancia_al_agujero
                ratones_salvados += 1
            else:
                break
        
        resultados.append(str(ratones_salvados))
    
    print("\n".join(resultados))

if __name__ == "__main__":
    resolver()