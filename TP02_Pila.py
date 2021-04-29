from pila import Pila
from random import randint

def barridoPila(pila : Pila):
    auxPila = Pila()

    while not pila.pila_vacia():
        num = pila.desapilar()
        print(num)
        auxPila.apilar(num)
    
    while not auxPila.pila_vacia():
        num = auxPila.desapilar()
        pila.apilar(num)

pilaRandom = Pila()

for i in range(10):
    pilaRandom.apilar(randint(0,100))


# Ejercicio 7
def eliminarIesimo(pila : Pila, iesimo : int):
    '''Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.'''
    pilaAux = Pila()
    
    if iesimo <= pila.tamanio() and iesimo > 0:
        for i in range(iesimo - 1):
            num = pila.desapilar()
            pilaAux.apilar(num)
        
        pila.desapilar()

        while not pilaAux.pila_vacia():
            num = pilaAux.desapilar()
            pila.apilar(num)

# barridoPila(pilaRandom)

# eliminarIesimo(pilaRandom, 2)

# print()
# barridoPila(pilaRandom)

# pilaNumeros = Pila()
# pilaAux = Pila()

# while True:
#     numero = int(input("Ingresar un numero distinto de 0: "))
    
#     if numero == 0:
#         break

#     if pilaNumeros.pila_vacia():
#         pilaNumeros.apilar(numero)
    
#     elif pilaNumeros.elemento_cima() <= numero:
#         pilaNumeros.apilar(numero)
    
#     else:
#         while not pilaNumeros.pila_vacia() and pilaNumeros.elemento_cima() >= numero:
#             num = pilaNumeros.desapilar()
#             pilaAux.apilar(num)

#         pilaNumeros.apilar(numero)

#         while not pilaAux.pila_vacia():
#             pilaNumeros.apilar(pilaAux.desapilar())

# pilaNumeros.barrido_pila()


# Ejercicio 16

pilaCapitulo_V = Pila()
pilaCapitulo_VII = Pila()
pila_intersec = Pila()

Capitulo_V = ['yoda','luke','leia','boba fett','darth vader','obi-wan']
Capitulo_VII = ['yoda','leia','obi-wan','finn','rey','kylo ren']

for cap in Capitulo_V:
    pilaCapitulo_V.apilar(cap)



for cap in Capitulo_VII:
    pilaCapitulo_VII.apilar(cap)

while(not pilaCapitulo_V.pila_vacia()):
    x = pilaCapitulo_V.elemento_cima()

    while( not pilaCapitulo_VII.pila_vacia()):
        c = pilaCapitulo_VII.desapilar()
        if x == c:
            pila_intersec.apilar(x)
        
    for cap in Capitulo_VII:
        pilaCapitulo_VII.apilar(cap)       

        
    x = pilaCapitulo_V.desapilar()
    

pila_intersec.barrido_pila()
           
          





    

    

