def diagonal_principal (matriz):
    vector_diagonal = []

    return vector_diagonal

def leer (ren, col):
    matriz = []

    return matriz

def main():
    ren = int(input())
    col = int(input())
    if (ren != col):
        print ("La matriz no es cuadrada")
    else:
        matriz = leer (ren, col)
        lista_diagonal = diagonal_principal(matriz)
        print (lista_diagonal)


if __name__=='__main__':
    main()
