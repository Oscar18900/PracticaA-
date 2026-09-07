import sys 
import time
import os
import heapq
from collections import deque

COSTOS = { 
    '.':1,
    ',': 5,   
    '~':10,
    'S':0,
    'G':0
} 

DIRECCIONES = [(1,0),(0,-1),(-1,0),(0,1)]
NOMBRES_DIRECCIONES = {
    (1,0):"ABAJO",
    (0,-1):"IZQUIERDA",
    (-1,0):"ARRIBA",
    (0,1):"DERECHA",    
    
}

def leer_laberinto(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = [linea.rstrip("\n") for linea in f if linea.strip("\n") != ""] 
 
    if not lineas:
        raise ValueError("El archivo del laberinto está vacío.")
 
    ancho = max(len(linea) for linea in lineas)
    matriz = [list(linea.ljust(ancho, "#")) for linea in lineas]
    return matriz

def encontrar_puntos(matriz):
    inicio = None
    meta = None 
    for f, fila in enumerate(matriz):
        for c, casilla in enumerate(fila):
            if casilla == "S":
                inicio = (f,c)
            elif casilla == "G":
                meta = (f,c)
    return inicio,meta


def calcular_costo(matriz, camino):
    return sum(COSTOS.get(matriz[f][c],1)for f,c in camino)

def obtener_pasos_direccion(camino):
    pasos = []
    for i in range(1,len(camino)):
        f0, c0 = camino[i-1]
        f1, c1 = camino[i]
        delta = (f1 - f0,c1 - c0)
        pasos.append(NOMBRES_DIRECCIONES.get(delta, "?"))
    return pasos

def main():
    carpeta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_por_defecto = os.path.join(carpeta_script, "laberinto_comparacion_BFS_DFS_UCS.txt")
    ruta_archivo = sys.argv[1] if len(sys.argv) > 1 else ruta_por_defecto
    
    try:
        matriz = leer_laberinto(ruta_archivo)
    except FileNotFoundError:
        print("No se encontro el archivo :v" )
        return
    
    inicio,meta = encontrar_puntos(matriz)
    if inicio is None or meta is None:
        print("No se encontró el punto de inicio (S) o la meta (G) en el laberinto.")
        return

    print (matriz)
if __name__ == "__main__":
    main()