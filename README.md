# Black-Jack
Mi dirección de github es
https://github.com/crltsnch/Black-Jack.git

Hemos resuel el juego de black jack.
El diagrama de flujo de este codigo es el siguie:

![Diagrama de flujo Black Jack](/Users/carlotasanchezgonzalez/Documents/Programación)

```
importar al  azar
de  randint de importación aleatoria  

cartas  = {
    chr ( 0x1f0a1 ): 11 ,
    chr ( 0x1f0a2 ): 2 ,
    chr ( 0x1f0a3 ): 3 ,
    chr ( 0x1f0a4 ): 4 ,
    chr ( 0x1f0a5 ): 5 ,
    chr ( 0x1f0a6 ): 6 ,
    chr ( 0x1f0a7 ): 7 ,
    chr ( 0x1f0a8 ): 8 ,
    chr ( 0x1f0a9 ): 9 ,
    chr ( 0x1f0aa ): 10 ,
    chr ( 0x1f0ab ): 10 ,
    chr ( 0x1f0ad ): 10 ,
    chr ( 0x1f0ae ): 10 ,
}

carta  =  cartas . llaves ()
listacartas  =  lista ( carta )
valor  =  cartas . valores ()
listavalor  =  lista ( valor )
imprimir ( listacartas )

print ( "1 \ Iteración estándar sobre un diccionario" )
para  carta , valor  en  cartas . elementos ():
    print ( "la carta {} vale {}" . formato ( carta , valor ))

print ( "2 \ Iteración ordenada sobre un diccionario" )
para  carta  en  ordenados ( listacartas ):
    print ( "la carta {} vale {}" . formato ( carta , cartas [ carta ]))

carta1jugador  =  aleatorio . randint ( 0 , 12 )
carta2jugador  =  aleatorio . randint ( 0 , 12 )
print ( "Las cartas que él elegido hijo:"  +  str ( listacartas [ carta1jugador ]) +  listacartas [ carta2jugador ])
print ( "Los valores de las cartas son respectivamente:"  +  str ( listavalor [ carta1jugador ]) + "y"  +  str ( listavalor [ carta2jugador ]))

carta1banca  =  aleatorio . randint ( 0 , 12 )
carta2banca  =  aleatorio . randint ( 0 , 12 )
print ( "Las cartas que ha elegido la banca son:"  +  str ( listacartas [ carta1banca ]) +  str ( listacartas [ carta2banca ]))
print ( "Los valores de las cartas elegidas por la banca son respectivamente:"  +  str ( listavalor [ carta1banca ]) +  "y"  +  str ( listavalor [ carta2banca ]))

mipuntuacion  =  listavalor [ carta1jugador ] +  listavalor [ carta2jugador ]
print ( "Mi puntuacion total es:"  +  str ( mipuntuacion ))
puntuacionbanca  =  listavalor [ carta1banca ] +  listavalor [ carta2banca ]
print ( "La puntuacion total de la banca es:"  +  str ( puntuacionbanca ))

si  puntuacionbanca  <  17 :
    print ( "La banca coge otra carta" )
    carta3banca  =  aleatorio . randint ( 0 , 12 )
    puntuacionbanca  =  puntuacionbanca  +  listavalor [ carta3banca ]
    print ( "La nueva puntuacion de la banca es:"  +  str ( puntuacionbanca ))
    

def  comparar ():
    si  mipuntuacion  ==  21  y  puntuacionbanca  <  mipuntuacion :
        print ( "¡He ganado!" )
    elif  mipuntuacion  ==  21  y  puntuacionbanca  ==  mipuntuacion :
        print ( "¡Empate!" )
    elif  mipuntuacion  ! =  21 :
        seguirjugando  =  input ( "¿Quieres coger otra carta? si / no:" )
        
        si  seguirjugando  ==  "si" :
            carta3jugador  =  aleatorio . randint ( 0 , 12 )
            nuevapuntuacion  =  listavalor [ carta1jugador ] +  listavalor [ carta2jugador ] +  listavalor [ carta3jugador ]
            print ( "El jugador coge otra carta" )
            print ( "Su nueva puntuacion es de:"  +  str ( nuevapuntuacion ))

            si  nuevapuntuacion  <  puntuacionbanca  o  nuevapuntuacion  >  21 :
                print ( "¡Has perdido!" )
            elif  nuevapuntuacion  ==  21  y  nuevapuntuacion  >  puntuacionbanca  o  nuevapuntuacion  >  puntuacionbanca :
                print ( "¡Has ganado!" )

        elif  seguirjugando  ==  "no" :
            si  puntuacionbanca  >  21  o  puntuacionbanca  <  mipuntuacion :
                print ( "¡Has ganado!" )
            elif  puntuacionbanca  >  mipuntuacion :
                print ( "¡Has perdido!" )
comparar ()
