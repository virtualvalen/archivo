
# -----------------------------------------------
# LABERINTO (BACKTRACKING) TODAS LAS SOLUCIONES
# -----------------------------------------------
''' Este código resuelve el problema del laberinto con backtracking iterativo,
    todas las soluciones encontradas las guarda en un archivo txt'''

MAX = int(input("ingrese las dimensiones del tablero: "))

mov_x = [0, 1, 0, -1]
mov_y = [1, 0, -1, 0]

# ---- Muestra el tablero ----
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(f"{c:2}" for c in fila))
    print("")

# Verifica si podemos movernos a esa celda
def es_valida(tablero, x, y):
    return 0 <= x < MAX and 0 <= y < MAX and tablero[x][y] != -1

# Coloca obstáculos manualmente
def colocar_obstaculos(tablero):
    tablero[0][3] = -1
    tablero[1][1] = -1
    tablero[2][1] = -1
    tablero[2][2] = -1
    tablero[2][3] = -1

def encontrar_caminos_iterativo(tablero):
    soluciones = []
    stack = []

    # Tablero auxiliar para marcar migas de pan
    tablero_aux = [[0]*MAX for _ in range(MAX)]
    tablero_aux[0][0] = 1   # primer paso

    # Pila contiene: (x, y, camino, tablero_aux_copia, paso)
    stack.append((0, 0, [(0,0)], tablero_aux, 1))

    while stack:
        x, y, camino, aux, paso = stack.pop()

        # Si llegamos al final, guardamos el camino
        if x == MAX - 1 and y == MAX - 1:
            soluciones.append(camino.copy())
            continue

        # Intentar las 4 direcciones
        for i in range(4):
            nx = x + mov_x[i]
            ny = y + mov_y[i]

            if es_valida(tablero, nx, ny) and aux[nx][ny] == 0:
                # Crear nueva copia del tablero auxiliar
                nuevo_aux = [fila.copy() for fila in aux]
                nuevo_aux[nx][ny] = paso + 1   # migas de pan: paso++

                nuevo_camino = camino + [(nx, ny)]

                # Apilar el nuevo estado
                stack.append((nx, ny, nuevo_camino, nuevo_aux, paso + 1))

    return soluciones

# Guarda los caminos encontrados
def guardar_en_txt(soluciones):
    with open("soluciones.txt", "w", encoding="utf-8") as f:
        if not soluciones:
            f.write("No hay caminos válidos.\n")
            return

        for i, camino in enumerate(soluciones, 1):

            f.write(f"Camino {i}:\n")
            f.write(" → ".join(str(p) for p in camino) + "\n")

            # Crear copia del tablero original con obstáculos
            tablero = [[0]*MAX for _ in range(MAX)]
            colocar_obstaculos(tablero)

            # Marcar el camino en el tablero copia
            paso = 1
            for (x, y) in camino:
                tablero[x][y] = paso
                paso += 1

            # Guardar el tablero en el archivo
            f.write("Tablero:\n")
            for fila in tablero:
                f.write(" ".join(f"{c:2}" for c in fila) + "\n")

            f.write("\n")  # Separación entre caminos

        f.write(f"Total de caminos encontrados: {len(soluciones)}\n")

# Programa principal
def main():
    tablero = [[0]*MAX for _ in range(MAX)]
    colocar_obstaculos(tablero)
    print("tablero con obstáculos:")
    mostrar_tablero(tablero)

    if tablero[0][0] == -1 or tablero[MAX-1][MAX-1] == -1:
        print("Inicio o fin bloqueado.")
        return
    soluciones = encontrar_caminos_iterativo(tablero)
    if soluciones:
        print(f"Se encontraron {len(soluciones)} caminos válidos.")
        mostrar_tablero(tablero)
    else:
        print("No se encontró ningún camino.")
    for i, camino in enumerate(soluciones, 1):
        print(f"Camino {i}:")
        copia = [fila.copy() for fila in tablero]
        paso = 1
        for (x, y) in camino:
            copia[x][y] = paso
            paso += 1
        for fila in copia:
            print(" ".join(f"{c:2}" for c in fila))
        print()

    guardar_en_txt(soluciones)
    print("Soluciones guardadas en 'soluciones.txt'.")

if __name__ == "__main__":
    main()