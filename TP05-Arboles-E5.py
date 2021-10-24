from arbol_binario import Arbol

#  Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
#  se (MCU), desarrollar un algoritmo que contemple lo siguiente:
#  a.además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
#  leano que indica si es un héroe o un villano, True y False respectivamente;
#  b.listar los villanos ordenados alfabéticamente;
#  c.mostrar todos los superhéroes que empiezan con C;
#  d.determinar cuántos superhéroes hay el árbol;
#  e.Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#  encontrarlo en el árbol y modificar su nombre;
#  f.listar los superhéroes ordenados de manera descendente;
#  g.generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#  los villanos, luego resolver las siguiente tareas:
#  I.
#  II.
#  6.
#  determinar cuántos nodos tiene cada árbol;
#  realizar un barrido ordenado alfabéticamente de cada árbol.
#  Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de naci-

villanos = [
    {'nombre' : 'Hulk', 'heroe' : True},
    {'nombre' : 'Thor', 'heroe' : True},
    {'nombre' : 'Capitan America', 'heroe' : True},
    {'nombre' : 'Dr. Strage', 'heroe' : False},
    {'nombre' : 'Thanos', 'heroe' : False}
]

arbolMCU = Arbol()

for villano in villanos:
    arbolMCU.insertar_nodo(villano['nombre'], villano)


#  Ejercicio b
#  arbolMCU.inorden()

#  Ejercicio c
#  arbolMCU.busqueda_proximidad('c')

#  ejercicio d
#  print(arbolMCU.contar_nodos())

#  ejercicio e
#  arbolMCU.inorden()
#  arbolMCU.remplazar_proximidad_MCU('Dr', 'Dr. Strange')
#  arbolMCU.inorden()

#  ejercicio f
# arbolMCU.postorden()

#  ejercicio g
arbol_villanos = Arbol()
arbol_heroes = Arbol()

arbolMCU.separar_heroes_villanos(arbol_villanos, arbol_heroes)

print('Arbol de villanos')
arbol_villanos.inorden()
print('Arbol de heroes')
arbol_heroes.inorden()

arbol_villanos.balancear()
arbol_heroes.balancear()


