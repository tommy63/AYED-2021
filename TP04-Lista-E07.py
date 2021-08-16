from lista import Lista, quicksort
from random import randint

# Implementar los algoritmos necesarios para resolver las siguientes tareas:

# a. concatenar dos listas, una atrás de la otra;
# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
# d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido

listaAleatoria1 = Lista()
listaAleatoria2 = Lista()
listaOrdenada = Lista()

repetidos = 0

# Cargar las dos listas con valores aleatorios
for i in range(10):
    listaAleatoria1.insertar(randint(0,25))
    listaAleatoria2.insertar(randint(0,25))

print("Lista 1:",listaAleatoria1)
print("Lista 2:",listaAleatoria2)

while not listaAleatoria1.lista_vacia():
    elemento = listaAleatoria1.eliminar_pos(0)
    print("Elemento eliminado:", elemento)
    if listaOrdenada.busqueda(elemento) == -1:
        listaOrdenada.insertar(elemento)
    else:
        repetidos += 1

while not listaAleatoria2.lista_vacia():
    elemento = listaAleatoria2.eliminar_pos(0)
    print("Elemento eliminado:", elemento)
    if listaOrdenada.busqueda(elemento) == -1:
        listaOrdenada.insertar(elemento)
    else:
        repetidos += 1

print("Lista ordenada:",listaOrdenada)
print("Elementos repetidos:", repetidos)
