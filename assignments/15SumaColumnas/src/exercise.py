
# leer elemento por elemento - 
def leer_matriz (renglon, columna):
    matriz = []
    for r in range(renglon):
        row = []
        for c in range(columna):
            valor = int(input())
            row.append(valor)
        matriz.append(row)  
    return matriz

def suma_columnas (matriz):
    lista_suma = []
    # Recorrido por columnas
    for c in range(len(matriz[0])):
        acum = 0
        for r in range(len(matriz)):
            # sacar el elemento  matriz[r][c]  - r, c
            acum = acum + matriz[r][c]
        
        # añadir a la lista_suma append
        lista_suma.append(acum)
        
    return lista_suma


def main():
    renglon = int(input())
    columna = int(input())
    if renglon >= 1 and columna >= 1:
        matriz = leer_matriz (renglon, columna)
        lista_suma = suma_columnas(matriz)
        print(lista_suma)
    else:
        print("Error")
