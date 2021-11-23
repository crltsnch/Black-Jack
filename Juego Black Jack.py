import random
from random import randint

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

carta=cartas.keys
listacartas=list(carta)
valor=carta.values
listapuntos=list(cartas.valores)
print(listacartas)
print(listapuntos)

print("1\ Iteración estándar sobre un diccionario")
for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))

print("2\ Iteración ordenada sobre un diccionario")
for carta in sorted(listacartas):
    print("la carta {} vale {}".format(carta, cartas[carta]))


print("Ha seleccionado:", end=" ")
carta1jugador = int(input(listacartas))
puntuacion = cartas[carta]
print(carta, end=" ")
carta2jugador = int(input(listacartas))
puntuacion += cartas[carta]
print(carta, end=" ")
print(" >>> su puntuación es de", puntuacion)

cartabanca1 = sample(listacartas)
puntuacionbanca = sum(cartas[carta] for carta in cartasbanca)
print("La banca tiene: {} {}  >> su score es {}".format(cartasbanca[0],
                                                          cartasbanca[1],
                                                          puntuacionbanca))