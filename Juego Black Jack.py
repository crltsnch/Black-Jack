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

print("1\ Iteración estándar sobre un diccionario")
for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))

print("2\ Iteración ordenada sobre un diccionario")
for carta in sorted(listacartas):
    print("la carta {} vale {}".format(carta, cartas[carta]))

carta1jugador = random.randint(0, 12)
carta2jugador = random.randint(0, 12)
print("Las cartas que he elegido son: " + str(listacartas[carta1jugador]) + listacartas[carta2jugador])
print( "Los valores de las cartas son respectivamente: " + str(listavalor[carta1jugador])+" y " + str(listavalor[carta2jugador]))

carta1banca = random.randint(0, 12)
carta2banca = random.randint(0, 12)
print("Las cartas que ha elegido la banca son: " + str(listacartas[carta1banca]) + str(listacartas[carta2banca]))
print("Los valores de las cartas elegidas por la banca son respectivamente: " + str(listavalor[carta1banca]) + " y " + str(listavalor[carta2banca]))

mipuntuacion = listavalor[carta1jugador] + listavalor[carta2jugador]
print("Mi puntuacion total es: " + str(mipuntuacion))
puntuacionbanca = listavalor[carta1banca]+ listavalor[carta2banca]
print("La puntuacion total de la banca es: " + str(puntuacionbanca))

if puntuacionbanca < 17:
    carta3banca = random.randint(0, 12)
    puntuacionbanca = puntuacionbanca + listavalor[carta3banca]
    print("La banca coge otra carta")


def comparar():
    if mipuntuacion == 21 and puntuacionbanca < mipuntuacion:
        print("¡He ganado!")
    elif mipuntuacion == 21 and puntuacionbanca == mipuntuacion:
        print("¡Empate!")
    if mipuntuacion != 21 and puntuacionbanca > mipuntuacion:
        seguirjugando = input("¿Quieres coger otra carta? si/no: ")

    if seguirjugando == "si" :
        carta3jugador = random.randint("Eliga una tercera carta de la lista de cartas: ")
        nuevapuntuacion = listavalor[carta1jugador] + listavalor[carta2jugador] + listavalor[carta3jugador]
        print("El jugador coge otra carta y su nueva puntuacion es de: " + str(nuevapuntuacion))

        if nuevapuntuacion < puntuacionbanca or nuevapuntuacion > 21:
            print("¡Has perdido!")
        elif nuevapuntuacion == 21 and nuevapuntuacion > puntuacionbanca or nuevapuntuacion > puntuacionbanca:
            print("¡Has ganado!")

    if seguirjugando == "no" :
        if puntuacionbanca > 22 or puntuacionbanca < mipuntuacion:
            print("¡Has ganado!")
        elif puntuacionbanca > mipuntuacion:
            print("¡Has perdido!")