# cantidad de filas
size = input("Dime el tamaño de tu piramide: ")

# comprobar tipo de dato del input
if type(size) != int:
    size = int(size)

for n in range(size):
    # primera fila
    if n == 0:
        print(" "*size + "*")

    # siguientes filas
    # iteraccion 'n' multiplica 'n' estrellas en cada lado dejando 'size-n' espacios al principio para centrar)
    # por ejemplo n = 3
    #     *
    #   * * *
    #  ** * **
    # *** * ***
    else:
        print(" "*(size-n) + "*" * n + "*" + "*" * n)








