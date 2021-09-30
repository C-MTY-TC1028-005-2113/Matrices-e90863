
# leer elemento por elemento - 
def leer_matriz (renglon, columna):
    matriz = []
    
    return matriz

def suma_columnas (matriz):
    lista_suma = []
    
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
