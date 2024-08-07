def pares_x_columna (matriz):
    # añadir instrucciones para formar la lista_pares

    return lista_pares

def leer_matriz(ren, col):
    matriz = []
    # añadir las instrucciones para leer_matriz

    return matriz

def main():
    # 1º Leer la cantidad de renglones y columnas
    ren = int(input())
    col = int(input())

    # 2º Llamar a la función leer que retorna una matriz ingresada del teclado
    matriz = leer_matriz (ren, col)

    # 3º Llamar pares_x_columna
    lista_pares = pares_x_columna(matriz)
    print (lista_pares)


if __name__=='__main__':
    main()
