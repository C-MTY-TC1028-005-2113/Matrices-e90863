def suma_matrices(matriz1, matriz2):
    matriz_suma = []
    
    return matriz_suma

def lee_matriz_por_renglon():
    matriz = []
    datos_renglon = input()

    return matriz

def main():
    matriz1 = lee_matriz_por_renglon()
    matriz2 = lee_matriz_por_renglon()
    if (len(matriz1) != len(matriz2) or
        len(matriz1[0]) != len(matriz2[0])):
        print("Las matrices no son del mismo tamaño")
    else:
        print(suma_matrices(matriz1,matriz2))


if __name__=='__main__':
    main()
