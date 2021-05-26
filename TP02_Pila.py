from pila import Pila, intercambiar_pila


# Ejercicio 14

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

# pilaCapitulo_V = Pila()
# pilaCapitulo_VII = Pila()
# pila_intersec = Pila()

# Capitulo_V = ['yoda','luke','leia','boba fett','darth vader','obi-wan']
# Capitulo_VII = ['yoda','leia','obi-wan','finn','rey','kylo ren']

# for cap in Capitulo_V:
#     pilaCapitulo_V.apilar(cap)



# for cap in Capitulo_VII:
#     pilaCapitulo_VII.apilar(cap)

# while(not pilaCapitulo_V.pila_vacia()):
#     x = pilaCapitulo_V.elemento_cima()

#     while( not pilaCapitulo_VII.pila_vacia()):
#         c = pilaCapitulo_VII.desapilar()
#         if x == c:
#             pila_intersec.apilar(x)
        
#     for cap in Capitulo_VII:
#         pilaCapitulo_VII.apilar(cap)       

        
#     x = pilaCapitulo_V.desapilar()
    

# pila_intersec.barrido_pila()



# Ejercicio 22

# class Nave(object):
#     def __init__(self, cazaRecompensas):
#         self.cazaRecompensas = cazaRecompensas
#         self.bitacora = Pila()

# class Mision(object):
#     def __init__(self, id, planetaVisitado, captura, recompensa):
#         self.id = id
#         self.planetaVisitado = planetaVisitado
#         self.captura = captura
#         self.recompensa = recompensa

# pilaMisiones = Pila()

# misiones = [
#     Mision(1,"asd", "qwe", 120),
#     Mision(2,"afe", "aseee", 150),
#     Mision(3,"asgfhr", "afghj", 130),
#     Mision(4,"asd12124", "qbnbv", 220)
# ]

# for mision in misiones:
#     pilaMisiones.apilar(mision)

# naves = [
#     Nave("Boba Fett"),
#     Nave("Din Djarin"),
#     Nave("Din Djarin"),
#     Nave("Boba Fett"),
# ]

# naves[0].bitacora.apilar(misiones[1], misiones[3])
# naves[1].bitacora.apilar(misiones[2], misiones[3], misiones[1])
# naves[2].bitacora.apilar(misiones[0], misiones[1])
# naves[3].bitacora.apilar(misiones[0], misiones[2], misiones[3])

# pilaNaves = Pila()
# pilaNavesBoba = Pila()
# pilaNavesDin = Pila()
# aux = Pila()

# recaudacionBoba = 0
# recaudacionDin = 0

# while not pilaNaves.pila_vacia():
#     naveActual = pilaNaves.desapilar()

#     if naveActual.cazaRecompensas == "Boba Fett":
#         pilaNavesBoba.apilar(naveActual)
#     else:
#         pilaNavesDin.apilar(naveActual)

# while not pilaNavesBoba.pila_vacia():
#     bitacoras_aux = Pila()
#     naveActual = pilaNavesBoba.desapilar()
#     while not naveActual.bitacoras.pila_vacia():
#         misionActual = naveActual.bitacoras.desapilar()

#         recaudacionBoba += misionActual.recompensa

#         bitacoras_aux.apilar(misionActual)
    
#         naveActual.bitacoras = intercambiar_pila(bitacoras_aux)
    
#     aux.apilar(naveActual)

# pilaNavesBoba = intercambiar_pila(aux)


# while not pilaNavesDin.pila_vacia():
#     bitacoras_aux = Pila()
#     naveActual = pilaNavesDin.desapilar()
#     while not naveActual.bitacoras.pila_vacia():
#         misionActual = naveActual.bitacoras.desapilar()

#         recaudacionDin += misionActual.recompensa

#         bitacoras_aux.apilar(misionActual)
    
#         naveActual.bitacoras = intercambiar_pila(bitacoras_aux)
    
#     aux.apilar(naveActual)

# pilaNavesDin = intercambiar_pila(aux)

# print("Boba Fett recaudo", recaudacionBoba , "creditos")
# print("Din Djarin recaudo", recaudacionDin , "creditos")

# if recaudacionBoba > recaudacionDin:
#     print("Boba Fett tuvo mayor recaudacion")
# elif(recaudacionDin > recaudacionBoba):
#     print("Din Djarin tuvo mayor recaudacion")
# else:
#     print("Los dos cazarecompensas recaudaron lo mismo")
          


# Ejercicio 24

class Personaje(object):
    def __init__(self, nombre, cantidadPeliculas):
        self.nombre = nombre
        self.cantidadPeliculas = cantidadPeliculas

    def __str__(self):
        return "Nombre: " + self.nombre + ", cantidad de peliculas: " + str(self.cantidadPeliculas)

def hallarPos(pila : Pila, personaje : str):
    aux = Pila()
    pos = 0
    i = 0

    while not pila.pila_vacia():
        i += 1

        perAux = pila.desapilar()
        aux.apilar(perAux)

        if perAux.nombre == personaje:
            pos = i

    while not aux.pila_vacia():
        pila.apilar(aux.desapilar())
    
    return pos

pilaPersonajes = Pila()
aux = Pila()

personajes = [
    Personaje("Black Widow", 7),
    Personaje("Groot", 4),
    Personaje("Rocket Raccoon", 6),
    Personaje("Capitan America", 10),
    Personaje("Dr. Strange", 2)
]

for personaje in personajes:
    pilaPersonajes.apilar(personaje)

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
# uno la cima de la pila;
print(hallarPos(pilaPersonajes, "Groot"))
print(hallarPos(pilaPersonajes, "Rocket Raccoon"))


# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
# la cantidad de películas en la que aparece;
while not pilaPersonajes.pila_vacia():
    personaje = pilaPersonajes.desapilar()
    aux.apilar(personaje)

    if personaje.cantidadPeliculas > 5:
        print(personaje)

pilaPersonajes = intercambiar_pila(aux)

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
while not pilaPersonajes.pila_vacia():
    personaje = pilaPersonajes.desapilar()
    aux.apilar(personaje)

    if personaje.nombre == "Black Widow":
        print(personaje.cantidadPeliculas)

pilaPersonajes = intercambiar_pila(aux)

#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
while not pilaPersonajes.pila_vacia():
    personaje = pilaPersonajes.desapilar()
    aux.apilar(personaje)

    if personaje.nombre[0] == "D" or personaje.nombre[0] == "C" or personaje.nombre[0] == "G":
        print(personaje.nombre)

pilaPersonajes = intercambiar_pila(aux)
    

    

