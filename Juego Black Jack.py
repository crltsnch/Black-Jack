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

carta = cartas.keys()
listacartas = list(carta)
valor = cartas.values()
listavalor = list(valor)
print(listacartas)
print(listavalor)

print("1\ Iteración estándar sobre un diccionario")
for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))

print("2\ Iteración ordenada sobre un diccionario")
for carta in sorted(listacartas):
    print("la carta {} vale {}".format(carta, cartas[carta]))

print("3\ Black Jack")
listacartas = list(carta)

carta1jugador = int(input("Eliga una carta de la lista de cartas: "))
puntuacion = listacartas[carta1jugador]
print(listacartas[carta1jugador])
carta2jugador = int(input("Elija otra carta de la lista de cartas: "))
puntuacion = listacartas[carta2jugador]
print(listacartas[carta2jugador])
mipuntuacion=listavalor[carta1jugador]+listavalor[carta2jugador]

print("La puntuacion de mis cartas son respectivamente: " + str(mipuntuacion))


carta1banca = random.randint(listacartas)
carta2banca = random.randint(listacartas)
cartasbanca = "carta1banca" + "carta2banca"
puntuacionbanca = listavalor[carta1banca]+ listavalor[carta2banca]
print("La banca tiene" + str(cartasbanca) + "y" + "su puntuacion es" + str(puntuacionbanca))