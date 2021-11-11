from grafo import Grafo
from math import sqrt

def distancia(coordOrigen, coordDest):
    x1 = coordOrigen[0]
    y1 = coordOrigen[1]
    x2 = coordDest[0]
    y2 = coordDest[1]

    return sqrt(pow((x2-x1), 2) + pow((y2 - y1), 2))

grafoTemplos = Grafo(dirigido=False)

templos = [
    { "templo" : "Partenón", "coord" : [2,5]},
    { "templo" : "Olimpia", "coord" : [5,3]},
    { "templo" : "Delfos", "coord" : [7,6]},
    { "templo" : "Sunión", "coord" : [2,7]},
    { "templo" : "Éfeso", "coord" : [0,3]},
    { "templo" : "Acrópolis", "coord" : [0,1]}
]

#  caminos = [
    #  {"origen" : "Partenón", "destino" : "Delfos"},
    #  {"origen" : "Delfos", "destino" : "Olimpia"},
    #  {"origen" : "Partenón", "destino" : "Olimpia"},
    #  {"origen" : "Sunión", "destino" : "Delfos"},
    #  {"origen" : "Éfeso", "destino" : "Delfos"},
    #  {"origen" : "Acrópolis", "destino" : "Olimpia"},
#  ]

for templo in templos:
    grafoTemplos.insertar_vertice(templo["templo"], data=templo)

for i in range(grafoTemplos.inicio.tamanio()):
    origen = grafoTemplos.inicio.obtener_elemento(i)
    for j in range(i+1, grafoTemplos.inicio.tamanio()):
        destino = grafoTemplos.inicio.obtener_elemento(j)
        coordOr = origen['data']['coord']
        coordDest = destino['data']['coord']
        grafoTemplos.insertar_arista(distancia(coordOr, coordDest), origen['info'], destino['info'])

#  ejercicio c
#  print("Arbol de expansión minima")
#  pos = grafoTemplos.buscar_vertice('Delfos')
#  print(grafoTemplos.prim(pos))

#  ejercicio d
#  posPartenon = grafoTemplos.buscar_vertice("Partenón")
#  posDelfos = grafoTemplos.buscar_vertice("Delfos")

#  pila_camino = grafoTemplos.dijkstra(posPartenon, posDelfos)

#  destino = 'Delfos'
#  costo = None
#  while(not pila_camino.pila_vacia()):
   #  dato = pila_camino.desapilar()
   #  if(dato[1][0] == destino):
       #  if(costo is None):
           #  costo = dato[0]
       #  print(dato[1][0])
       #  destino = dato[1][1]
#  print('el costo total del camino es:', costo)
