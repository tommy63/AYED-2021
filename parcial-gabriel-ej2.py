
from grafo import Grafo


#  Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
#  necesarios para resolver las tareas, listadas a continuación:
#  1. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;

equipos = [
    ['Ubuntu', 'PC'],
    ['Debian', 'Notebook'],
    ['Impresora', 'Impresora'],
    ['Mint', 'PC'],
    ['Switch 1', 'Switch'],
    ['Router 1', 'Router'],
    ['Router 2', 'Router'],
    ['Router 3', 'Router'],
    ['Red Hat', 'Notebook'],
    ['Guarani', 'Servidor'],
    ['Manjaro', 'PC'],
    ['Fedora', 'PC'],
    ['Switch 2', 'Switch'],
    ['Parrot', 'PC'],
    ['MongoDB', 'Servidor'],
    ['Arch', 'Notebook']
]

conexiones = [
    ['Ubuntu', 'Switch 1', 18],
    ['Debian', 'Switch 1', 17],
    ['Impresora', 'Switch 1', 22],
    ['Mint', 'Switch 1', 80],
    ['Switch 1', 'Router 1', 29],
    ['Router 2', 'Router 1', 29],
    ['Router 3', 'Router 1', 43],
    ['Router 3', 'Router 2', 50],
    ['Red Hat', 'Router 2', 25],
    ['Guarani', 'Router 2', 9],
    ['Switch 2', 'Router 3', 61],
    ['Switch 2', 'Manjaro', 40],
    ['Switch 2', 'Parrot', 12],
    ['Switch 2', 'MongoDB', 5],
    ['Switch 2', 'Arch', 56],
    ['Switch 2', 'Fedora', 3]
]

grafoSistema = Grafo(dirigido=False)

for equipo in equipos:
    grafoSistema.insertar_vertice(equipo[0], data=equipo)

for conexion in conexiones:
    grafoSistema.insertar_arista(conexion[2], conexion[0], conexion[1])

#  2. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
#  Hat, Debian, Arch;
#  pos = grafoSistema.buscar_vertice('Debian')
#  grafoSistema.barrido_profundidad(pos)
#  pos = grafoSistema.buscar_vertice('Red Hat')
#  grafoSistema.barrido_profundidad(pos)
#  pos = grafoSistema.buscar_vertice('Arch')
#  grafoSistema.barrido_profundidad(pos)

#  pos = grafoSistema.buscar_vertice('Debian')
#  grafoSistema.barrido_amplitud(pos)
#  pos = grafoSistema.buscar_vertice('Red Hat')
#  grafoSistema.barrido_amplitud(pos)
#  pos = grafoSistema.buscar_vertice('Arch')
#  grafoSistema.barrido_amplitud(pos)

#  3. encontrar el camino más corto para enviar a imprimir un documento desde la pc:
#  Debian y Red Hat, hasta el servidor “MongoDB”;
#  posDebian = grafoSistema.buscar_vertice("Debian")
#  posRedHat = grafoSistema.buscar_vertice("Red Hat")
#  posMongo = grafoSistema.buscar_vertice("MongoDB")

#  pila_camino1 = grafoSistema.dijkstra(posDebian, posMongo)
#  pila_camino2 = grafoSistema.dijkstra(posRedHat, posMongo)

#  destino = 'MongoDB'
#  encontrarDestino = False
#  while ( not pila_camino2.pila_vacia() ):
    #  dato = pila_camino2.desapilar()[1][0]
    #  if dato == destino:
        #  encontrarDestino = True
    #  if encontrarDestino:
        #  print(dato)

#  encontrarDestino = False
#  while ( not pila_camino1.pila_vacia() ):
    #  dato = pila_camino1.desapilar()[1][0]
    #  if dato == destino:
        #  encontrarDestino = True
    #  if encontrarDestino:
        #  print(dato)


#  4. encontrar el árbol de expansión mínima;
#  print(grafoSistema.prim(0))

#  5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
#  realice un barrido en profundidad para corroborar que efectivamente fue borrada;
#  grafoSistema.eliminar_vertice('Impresora')
#  grafoSistema.barrido_profundidad(0)

