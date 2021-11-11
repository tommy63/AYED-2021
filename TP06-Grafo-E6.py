from grafo import Grafo


grafoDioses = Grafo(dirigido=False)


grafoDioses.insertar_vertice('Gaia')
grafoDioses.insertar_vertice('Urano')

grafoDioses.insertar_vertice('Themis')
grafoDioses.insertar_vertice('Minemosyne')
grafoDioses.insertar_vertice('Hyperion')
grafoDioses.insertar_vertice('Theia')
grafoDioses.insertar_vertice('Crios')
grafoDioses.insertar_vertice('Cronos')
grafoDioses.insertar_vertice('Rhea')
grafoDioses.insertar_vertice('Kdios')
grafoDioses.insertar_vertice('Phoibe')
grafoDioses.insertar_vertice('Iapetos')
grafoDioses.insertar_vertice('Okeanos')
grafoDioses.insertar_vertice('Tedds')

grafoDioses.insertar_vertice('Helios')
grafoDioses.insertar_vertice('Eos')
grafoDioses.insertar_vertice('Selene')
grafoDioses.insertar_vertice('Prometheus')
grafoDioses.insertar_vertice('Epimetheus')
grafoDioses.insertar_vertice('Atlas')
grafoDioses.insertar_vertice('Pleione')

grafoDioses.insertar_vertice('Hades')
grafoDioses.insertar_vertice('Demeter')
grafoDioses.insertar_vertice('Poseidon')
grafoDioses.insertar_vertice('Hestia')
grafoDioses.insertar_vertice('Hera')
grafoDioses.insertar_vertice('Zeus')
grafoDioses.insertar_vertice('Leto')
grafoDioses.insertar_vertice('Semelle')
grafoDioses.insertar_vertice('Maia')

grafoDioses.insertar_vertice('Persephone')
grafoDioses.insertar_vertice('Aphrodite')
grafoDioses.insertar_vertice('Ares')
grafoDioses.insertar_vertice('Hephaistos')
grafoDioses.insertar_vertice('Athena')
grafoDioses.insertar_vertice('Apollo')
grafoDioses.insertar_vertice('Artemis')
grafoDioses.insertar_vertice('Dionysos')
grafoDioses.insertar_vertice('Hermes')
grafoDioses.insertar_vertice('Penelopeia')

grafoDioses.insertar_vertice('Phobos')
grafoDioses.insertar_vertice('Deimos')
grafoDioses.insertar_vertice('Eros')
grafoDioses.insertar_vertice('Himeros')

grafoDioses.insertar_vertice('Hermaphrodite')
grafoDioses.insertar_vertice('Pan')

grafoDioses.insertar_arista(1, 'Urano', 'Gaia', data={'relacion': ['hijo', 'madre', 'pareja']})

grafoDioses.insertar_arista(1, 'Urano', 'Themis', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Urano', 'Hyperion', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Urano', 'Theia', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Urano', 'Crios', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Urano', 'Cronos', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Urano', 'Rhea', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Urano', 'Iapetos', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Urano', 'Okeanos', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Urano', 'Tedds', data={'relacion': ['padre', 'hijo']})

grafoDioses.insertar_arista(1, 'Gaia', 'Themis', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Gaia', 'Hyperion', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Gaia', 'Theia', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Gaia', 'Crios', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Gaia', 'Cronos', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Gaia', 'Rhea', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Gaia', 'Iapetos', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Gaia', 'Okeanos', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Gaia', 'Tedds', data={'relacion': ['madre', 'hijo']})


grafoDioses.insertar_arista(1, 'Hyperion', 'Theia', data={'relacion': ['pareja', 'hermano']})

grafoDioses.insertar_arista(1, 'Hyperion', 'Helios', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Hyperion', 'Eos', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Hyperion', 'Selene', data={'relacion': ['padre', 'hijo']})

grafoDioses.insertar_arista(1, 'Theia', 'Helios', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Theia', 'Eos', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Theia', 'Selene', data={'relacion': ['madre', 'hijo']})

grafoDioses.insertar_arista(1, 'Iapetos', 'Prometheus', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Iapetos', 'Epimetheus', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Iapetos', 'Atlas', data={'relacion': ['padre', 'hijo']})


grafoDioses.insertar_arista(1, 'Okeanos', 'Tedds', data={'relacion': ['pareja', 'hermano']})

grafoDioses.insertar_arista(1, 'Okeanos', 'Pleione', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Tedds', 'Pleione', data={'relacion': ['madre', 'hijo']})


grafoDioses.insertar_arista(1, 'Cronos', 'Rhea', data={'relacion': ['pareja', 'hermano']})

grafoDioses.insertar_arista(1, 'Cronos', 'Hades', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Cronos', 'Demeter', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Cronos', 'Poseidon', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Cronos', 'Hestia', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Cronos', 'Hera', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Cronos', 'Zeus', data={'relacion': ['padre', 'hijo']})

grafoDioses.insertar_arista(1, 'Rhea', 'Hades', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Rhea', 'Demeter', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Rhea', 'Poseidon', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Rhea', 'Hestia', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Rhea', 'Hera', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Rhea', 'Zeus', data={'relacion': ['madre', 'hijo']})


grafoDioses.insertar_arista(1, 'Kdios', 'Phoibe', data={'relacion': ['pareja', 'hermano']})

grafoDioses.insertar_arista(1, 'Kdios', 'Leto', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Phoibe', 'Leto', data={'relacion': ['madre', 'hijo']})


grafoDioses.insertar_arista(1, 'Atlas', 'Pleione', data={'relacion': ['pareja', 'hermano']})

grafoDioses.insertar_arista(1, 'Atlas', 'Maia', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Pleione', 'Maia', data={'relacion': ['madre', 'hijo']})


grafoDioses.insertar_arista(1, 'Demeter', 'Zeus', data={'relacion': ['pareja', 'hermano']})

grafoDioses.insertar_arista(1, 'Demeter', 'Persephone', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Zeus', 'Persephone', data={'relacion': ['padre', 'hijo']})


grafoDioses.insertar_arista(1, 'Hera', 'Zeus', data={'relacion': ['pareja', 'hermano']})

grafoDioses.insertar_arista(1, 'Hera', 'Ares', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Hera', 'Hephaistos', data={'relacion': ['madre', 'hijo']})

grafoDioses.insertar_arista(1, 'Zeus', 'Ares', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Zeus', 'Hephaistos', data={'relacion': ['padre', 'hijo']})


grafoDioses.insertar_arista(1, 'Zeus', 'Athena', data={'relacion': ['pareja']})


grafoDioses.insertar_arista(1, 'Zeus', 'Leto', data={'relacion': ['pareja']})

grafoDioses.insertar_arista(1, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Zeus', 'Artemis', data={'relacion': ['padre', 'hijo']})

grafoDioses.insertar_arista(1, 'Leto', 'Apollo', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Leto', 'Artemis', data={'relacion': ['madre', 'hijo']})


grafoDioses.insertar_arista(1, 'Zeus', 'Semelle', data={'relacion': ['pareja']})

grafoDioses.insertar_arista(1, 'Zeus', 'Dionysos', data={'relacion': ['padre', 'hijo']})

grafoDioses.insertar_arista(1, 'Semelle', 'Dionysos', data={'relacion': ['madre', 'hijo']})


grafoDioses.insertar_arista(1, 'Zeus', 'Maia', data={'relacion': ['pareja']})

grafoDioses.insertar_arista(1, 'Zeus', 'Hermes', data={'relacion': ['padre', 'hijo']})

grafoDioses.insertar_arista(1, 'Maia', 'Hermes', data={'relacion': ['madre', 'hijo']})


grafoDioses.insertar_arista(1, 'Hades', 'Persephone', data={'relacion': ['pareja']})


grafoDioses.insertar_arista(1, 'Aphrodite', 'Ares', data={'relacion': ['pareja']})

grafoDioses.insertar_arista(1, 'Aphrodite', 'Phobos', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Aphrodite', 'Deimos', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Aphrodite', 'Eros', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Aphrodite', 'Himeros', data={'relacion': ['padre', 'hijo']})

grafoDioses.insertar_arista(1, 'Ares', 'Phobos', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Ares', 'Deimos', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Ares', 'Eros', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Ares', 'Himeros', data={'relacion': ['madre', 'hijo']})


grafoDioses.insertar_arista(1, 'Aphrodite', 'Hephaistos', data={'relacion': ['pareja']})


grafoDioses.insertar_arista(1, 'Aphrodite', 'Hermes', data={'relacion': ['pareja']})

grafoDioses.insertar_arista(1, 'Aphrodite', 'Hermaphrodite', data={'relacion': ['madre', 'hijo']})

grafoDioses.insertar_arista(1, 'Hermes', 'Hermaphrodite', data={'relacion': ['padre', 'hijo']})


grafoDioses.insertar_arista(1, 'Hermes', 'Penelopeia', data={'relacion': ['pareja']})

grafoDioses.insertar_arista(1, 'Hermes', 'Pan', data={'relacion': ['padre', 'hijo']})

grafoDioses.insertar_arista(1, 'Penelopeia', 'Pan', data={'relacion': ['madre', 'hijo']})


grafoDioses.insertar_arista(1, 'Themis', 'Minemosyne', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Themis', 'Hyperion', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Themis', 'Theia', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Themis', 'Crios', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Themis', 'Cronos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Themis', 'Rhea', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Themis', 'Kdios', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Themis', 'Phoibe', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Themis', 'Iapetos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Themis', 'Okeanos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Themis', 'Tedds', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Minemosyne', 'Hyperion', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Minemosyne', 'Theia', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Minemosyne', 'Crios', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Minemosyne', 'Cronos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Minemosyne', 'Rhea', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Minemosyne', 'Kdios', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Minemosyne', 'Phoibe', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Minemosyne', 'Iapetos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Minemosyne', 'Okeanos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Minemosyne', 'Tedds', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Hyperion', 'Crios', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Hyperion', 'Cronos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Hyperion', 'Rhea', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Hyperion', 'Kdios', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Hyperion', 'Phoibe', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Hyperion', 'Iapetos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Hyperion', 'Okeanos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Hyperion', 'Tedds', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Theia', 'Cronos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Theia', 'Rhea', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Theia', 'Kdios', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Theia', 'Phoibe', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Theia', 'Iapetos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Theia', 'Okeanos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Theia', 'Tedds', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Cronos', 'Rhea', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Cronos', 'Kdios', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Cronos', 'Phoibe', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Cronos', 'Iapetos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Cronos', 'Okeanos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Cronos', 'Tedds', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Kdios', 'Phoibe', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Kdios', 'Iapetos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Kdios', 'Okeanos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Kdios', 'Tedds', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Phoibe', 'Iapetos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Phoibe', 'Okeanos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Phoibe', 'Tedds', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Iapetos', 'Okeanos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Iapetos', 'Tedds', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Okeanos', 'Tedds', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Helios', 'Eos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Helios', 'Selene', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Eos', 'Selene', data={'relacion': ['hermano']})


grafoDioses.insertar_arista(1, 'Prometheus', 'Epimetheus', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Prometheus', 'Atlas', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Epimetheus', 'Atlas', data={'relacion': ['hermano']})


grafoDioses.insertar_arista(1, 'Hades', 'Demeter', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Hades', 'Poseidon', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Hades', 'Hestia', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Hades', 'Hera', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Hades', 'Zeus', data={'relacion': ['hermano']})


grafoDioses.insertar_arista(1, 'Demeter', 'Poseidon', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Demeter', 'Hestia', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Demeter', 'Hera', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Poseidon', 'Hestia', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Poseidon', 'Hera', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Poseidon', 'Zeus', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Hestia', 'Hera', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Hestia', 'Zeus', data={'relacion': ['hermano']})


grafoDioses.insertar_arista(1, 'Ares', 'Hephaistos', data={'relacion': ['hermano']})


grafoDioses.insertar_arista(1, 'Apollo', 'Artemis', data={'relacion': ['hermano']})


grafoDioses.insertar_arista(1, 'Phobos', 'Deimos', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Phobos', 'Eros', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Phobos', 'Himeros', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Deimos', 'Eros', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Deimos', 'Himeros', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Eros', 'Himeros', data={'relacion': ['hermano']})




# a. además del nombre de los dioses, deberá cargar una breve descripción de quien es o lo que
# representa, no más de 20 palabras;

# for i in range(grafoDioses.tamanio()):
#     dios = grafoDioses.inicio.obtener_elemento(i)
#     if dios:
#         dios['data'] = {'descripcion': input('agregar descripcion')}

# grafoDioses.barrido_vertices()





# c. dado el nombre de un dios mostrar los hijos de este;

# nombre = input('Nombre del dios: ')

# for i in range(grafoDioses.tamanio()):
#     dios = grafoDioses.inicio.obtener_elemento(i)
#     if dios['info'] == nombre:
#         for j in range(dios['aristas'].tamanio()):
#             arista = dios['aristas'].obtener_elemento(j)
#             if(len(arista['data']['relacion']) == 2 and arista['data']['relacion'][1] == 'hijo'):
#                 print(arista)
            

# d. dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos;

# grafoDioses.adyacentes('Zeus')


# e. determinar si existe relación directa entre dos vértice cualquieras, de ser así cual es la relación
# entre ambos;

# def directo(ver_origen, ver_destino):
#     print('tiene relacion directa:')
#     pos = grafoDioses.buscar_arista(ver_origen, ver_destino)
#     if(pos != 1):
#         pos_aux = grafoDioses.buscar_vertice(ver_origen)
#         print(grafoDioses.inicio.obtener_elemento(pos_aux)['aristas'].obtener_elemento(pos))


# directo('Hades', 'Persephone')



# f. dados dos dioses determinar el camino más corto entre estos y mostrarlo. Considere como
# camino más corto el que tenga menor número de aristas;

# def camino_entre_dioses(origen, destino):

#     ver_origen = grafoDioses.buscar_vertice(origen)
#     ver_destino = grafoDioses.buscar_vertice(destino)
#     costo = None
    
#     if ver_origen != -1 and ver_destino != -1:
#         camino = grafoDioses.dijkstra(ver_origen)
        
#         while(not camino.pila_vacia()):
#             dato = camino.desapilar()
#             if(dato[1][0] == destino):
#                 if(costo is None):
#                     costo = dato[0]
#                 print('paso por: ', dato[1][0])
                        
#         print('el costo total del camino es: ', costo)

# camino_entre_dioses('Hades','Zeus')

# g. realizar un barrido en profundidad y amplitud de dicho grafo;

# grafoDioses.barrido_profundidad(0)
# print()
# grafoDioses.barrido_amplitud(0)


# h. realizar un barrido mostrando el nombre de cada dios y el de su madre;

# def buscar_madre(ver_origen, nombre_relacion):
#     pos_origen = grafoDioses.buscar_vertice(ver_origen)
#     if pos_origen != -1:
#         dios = grafoDioses.inicio.obtener_elemento(pos_origen)
#         for i in range(dios['aristas'].tamanio()):
#             relacion = dios['aristas'].obtener_elemento(i)['data']['relacion']
#             if ((len(relacion) > 1) and (relacion[1] == nombre_relacion)):
#                 return  dios['aristas'].obtener_elemento(i)['destino']
#     else:
#         return None

# for i in range(grafoDioses.tamanio()):
#     dios = grafoDioses.inicio.obtener_elemento(i)['info']
#     if buscar_madre(dios,'madre') == None:
#         print('El dios ',dios,'no tiene madre')
#         print()
#     else:
#         print('La mama del dios: ',dios,'es ')
#         print(buscar_madre(dios,'madre'))

# i. mostrar todos los ancestros de un determinado dios;

# def ancestro(vertice_nombre):
#     origen = grafoDioses.buscar_vertice(vertice_nombre)
#     if(origen != -1):
#         dios = grafoDioses.inicio.obtener_elemento(origen)
#         for i in range(dios['aristas'].tamanio()):
#             nombre_dios = dios['aristas'].obtener_elemento(i)['destino']
#             dios_aux = dios['aristas'].obtener_elemento(i)['data']
#             if(len(dios_aux['relacion']) == 2):
#                 if(dios_aux['relacion'][1] == 'padre' or dios_aux['relacion'][1] == 'madre'):
#                     print(nombre_dios, dios_aux['relacion'])
#                     ancestro(nombre_dios)

# ancestro('Zeus')


# j. mostrar todos los nietos de Cronos;



# k. mostrar todos los hijos de Tea;