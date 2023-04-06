# Dada la siguiente lista de números, realiza la suma de todos los números pares e impares*
# por separado en las variables suma_pares y suma_impares respectivamente:
# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
# *Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es
# cero cuando dicho valor es par, y 1 cuando es impar
# num % 2 == 0 (valores pares)
# num % 2 == 1 (valores impares)


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    # es par
    if num % 2 == 0:
        suma_pares = suma_pares + num

    # es impar
    else:
        suma_impares = suma_impares + num

