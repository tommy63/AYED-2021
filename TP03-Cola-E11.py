# Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:

# a.mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b.indicar el plantea natal de Luke Skywalker y Han Solo
# c.insertar un nuevo personaje antes del maestro Yoda
# d.eliminar el personaje ubicado después de Jar Jar Binks

from cola import Cola

class Personaje(object):
    def __init__(self, nombre : str, planeta : str):
        self.nombre = nombre
        self.planeta = planeta
    def __str__(self) -> str:
        return "Personaje: " + self.nombre + ", Planeta: " + self.planeta

colaPersonajes = Cola()

personajes = [
    Personaje("Yoda", "Alderaan"),
    Personaje("Luke Skywalker", "Alderaan")
]

for personaje in personajes:
    colaPersonajes.arribo(personaje)

# a.mostrar los personajes del planeta Alderaan, Endor y Tatooine
print("Personajes del planeta Alderaan, Endor y Tatooine")
for i in range(colaPersonajes.tamanio()):
    personaje : Personaje = colaPersonajes.mover_final()

    if personaje.planeta == "Alderaan" or personaje.planeta == "Endor" or personaje.planeta == "Tatooine":
        print(personaje)

print()

# b.indicar el plantea natal de Luke Skywalker y Han Solo
for i in range(colaPersonajes.tamanio()):
    personaje : Personaje = colaPersonajes.mover_final()

    if personaje.nombre == "Luke Skywalker":
        print("Planeta natal de Luke Skywalker: ", personaje.planeta)
    if personaje.nombre == "Han Solo":
        print("Planeta natal de Han Solo: ", personaje.planeta)

# c.insertar un nuevo personaje antes del maestro Yoda
for i in range(colaPersonajes.tamanio()):
    personaje : Personaje = colaPersonajes.en_frente()

    if personaje.nombre == "Yoda":
        print("Insertar un nuevo personaje antes del maestro Yoda")

        colaPersonajes.arribo(Personaje(
            input("Ingresar nombre: "),
            input("Ingresar planeta: ")
        ))
    colaPersonajes.mover_final()

# d.eliminar el personaje ubicado después de Jar Jar Binks
i = 0
while i < colaPersonajes.tamanio():
    personaje : Personaje = colaPersonajes.mover_final()

    if personaje.nombre == "Jar Jar Blinks" and i < colaPersonajes.tamanio() - 1:
        personaje = colaPersonajes.atencion()

        print("El personaje", personaje.nombre, "fue eliminado de la cola")

        i += 1

    i+=1
