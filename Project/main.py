# usuario introduce su nombre
# el programa pensara un numero del 1 al 100 que el usuario tendra que adivinar
# el usuario tendra 8 intentos para adivinarlo
# en cada intento el usuario dira un numero y el programa respondera cuatro cosas segun el numero dado:
    # si se sale de los limites, responder no esta permitido
    # si es menor que el secreto, responder que es menor
    # si es mayor que el secreto, responder que es mayor
    # si lo acierta, responder que ha ganado y decir cuantos intentos ha tardado
# por cada intento, repetir hasta que acierte o se acaben intentos

from random import randint

print("\nJUEGO DE LA PATATA CALIENTE")
print("¡En este juego deberás adivinar el número entre 1 y 100 que he pensado para ti!")

print("\nREGISTRAR JUGADOR")
jugador = input("Dime tu nombre: ")

print("\nCOMIENZA LA PARTIDA")
print("Acabo de pensar un número para ti")
secreto = randint(1,100)
intentos = 8
veces_necesitadas = 0

while intentos > 0:
    print("\nSEGUIMOS JUGANDO")
    respuesta = int(input(f"Dime tu número {jugador}: "))
    if respuesta < 1 or respuesta > 100:
        print(f"¡{respuesta} no está entre 1 y 100! Te quedan {intentos} intentos {jugador}")
    elif secreto > respuesta:
        print(f"¡Es mayor que {respuesta}! Te quedan {intentos} intentos {jugador}")
    elif secreto < respuesta:
        print(f"¡Es menor que {respuesta}! Te quedan {intentos} intentos {jugador}")
    else:
        print("\nFIN DE LA PARTIDA")
        print(f"¡Enhorabuena! {respuesta} es el número que había pensado. {jugador} lo ha resuelto en {veces_necesitadas} intentos")
        break
    intentos -= 1
    veces_necesitadas += 1
else:
    print("\nFIN DE LA PARTIDA")
    print(f"Se han acabado los intentos, el jugador '{jugador}' pierde la partida. El número era {secreto}")

