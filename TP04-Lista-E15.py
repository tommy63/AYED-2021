from lista import Lista,quicksort

ListaEntrenadores = Lista()


Entrenadores = [
    { 'nombre' : 'ash','torneos ganados' : 1,'B-perdidas' : 5,'B-ganadas' : 8 ,'pokemones' : Lista()},
    { 'nombre' : 'misty','torneos ganados' : 0,'B-perdidas' : 3,'B-ganadas' : 7 ,'pokemones' : Lista()},
    { 'nombre' : 'rojo','torneos ganados' : 8,'B-perdidas' : 0,'B-ganadas' : 10 ,'pokemones' : Lista()}
]


pokemon1 = {'nombre' : 'pikachu','nivel': 16,'tipo' : 'electrico', 'subtipo' : 'luchador'}
pokemon2 = {'nombre' : 'charmander','nivel': 15,'tipo' : 'fuego', 'subtipo' : ''}
pokemon3 = {'nombre' : 'squartul','nivel': 18,'tipo' : 'agua', 'subtipo' : ''}
pokemon4 = {'nombre' : 'sindaquil','nivel': 20,'tipo' : 'fuego', 'subtipo' : ''}
pokemon5 = {'nombre' : 'hitmonlee','nivel': 33,'tipo' : 'luchador', 'subtipo' : 'roca'}
pokemon6 = {'nombre' : 'wingull','nivel': 16,'tipo' : 'agua', 'subtipo' : 'volador'}
pokemon7 = {'nombre' : 'tyrantrum','nivel': 160,'tipo' : 'roca', 'subtipo' : 'dragon'}




for entrenador in Entrenadores:
    ListaEntrenadores.insertar(entrenador , 'nombre')

pos = ListaEntrenadores.busqueda('ash', 'nombre')
if pos != -1:
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon1, 'nombre')
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon4, 'nombre')

pos = ListaEntrenadores.busqueda('misty', 'nombre')
if pos != -1:
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon3, 'nombre')
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon6, 'nombre')

pos = ListaEntrenadores.busqueda('rojo', 'nombre')
if pos != -1:
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon2, 'nombre')
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon5, 'nombre')
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon7, 'nombre')


# a. obtener la cantidad de Pokémons de un determinado entrenador;

print('ingrese el entrenador')
entrena = input()
if entrena == 'ash':
    print(ListaEntrenadores.obtener_elemento(ListaEntrenadores.busqueda('ash','nombre'))['pokemones'].tamanio())
elif entrena == 'misty':
    print(ListaEntrenadores.obtener_elemento(ListaEntrenadores.busqueda('misty','nombre'))['pokemones'].tamanio())
elif entrena == 'rojo':
    print(ListaEntrenadores.obtener_elemento(ListaEntrenadores.busqueda('rojo','nombre'))['pokemones'].tamanio())
else:
    print('el nombre de entrenador no se encuentra')

print()
# b. listar los entrenadores que hayan ganado más de tres torneos;

for i in range(ListaEntrenadores.tamanio()):
    ganador = ListaEntrenadores.obtener_elemento(i)
    if ganador['torneos ganados'] >= 3 :
        print(ganador)

print()
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;

for i in range(ListaEntrenadores.tamanio()):
    ganador = ListaEntrenadores.obtener_elemento(i)
    if ganador['torneos ganados'] >= 3 :
        print(ganador)