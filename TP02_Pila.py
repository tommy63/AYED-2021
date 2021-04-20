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


