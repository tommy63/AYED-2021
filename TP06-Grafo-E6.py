from grafo import Grafo


grafoDioses = Grafo(dirigido=False)



grafoDioses.insertar_vertice('Urano')
grafoDioses.insertar_vertice('Cronos')
grafoDioses.insertar_vertice('Rea')
grafoDioses.insertar_vertice('Zeus')
grafoDioses.insertar_vertice('Hades')
grafoDioses.insertar_vertice('Demeter')
grafoDioses.insertar_vertice('Atenea')
grafoDioses.insertar_vertice('Apollo')
grafoDioses.insertar_vertice('Persefone')


# b. deberá cargar todas las relaciones entre los distintos dioses: padre, madre, hijo, hermano,
# pareja, la etiquetas de dichas aristas son estos nombre de relación.

grafoDioses.insertar_arista(1, 'Urano', 'Cronos', data={'relacion': ['padre', 'hijo']})

grafoDioses.insertar_arista(1, 'Cronos', 'Zeus', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Cronos', 'Hades', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Cronos', 'Demeter', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Cronos', 'Rea', data={'relacion': ['pareja']})
grafoDioses.insertar_arista(1, 'Cronos', 'Rea', data={'relacion': ['hermano']})

grafoDioses.insertar_arista(1, 'Zeus', 'Hades', data={'relacion': ['hermano']})
grafoDioses.insertar_arista(1, 'Zeus', 'Atenea', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})
grafoDioses.insertar_arista(1, 'Zeus', 'Persefone', data={'relacion': ['padre', 'hijo']})

grafoDioses.insertar_arista(1, 'Demeter', 'Persefone', data={'relacion': ['madre', 'hijo']})
grafoDioses.insertar_arista(1, 'Apollo', 'Persefone', data={'relacion': ['hermano']})


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
#     print(pos)
#     if(pos != 1):
#         pos_aux = grafoDioses.buscar_vertice('Cronos')
#         print(grafoDioses.inicio.obtener_elemento(pos_aux)['aristas'].obtener_elemento(pos))


# directo('Cronos', 'Zeus')



# f. dados dos dioses determinar el camino más corto entre estos y mostrarlo. Considere como
# camino más corto el que tenga menor número de aristas;




# g. realizar un barrido en profundidad y amplitud de dicho grafo;

# grafoDioses.barrido_profundidad(0)
# print()
# grafoDioses.barrido_amplitud(0)


# h. realizar un barrido mostrando el nombre de cada dios y el de su madre;



# i. mostrar todos los ancestros de un determinado dios;

# def ancestro(vertice_nombre):
#     origen = grafoDioses.buscar_vertice(vertice_nombre)
#     if(origen != -1):
#         dios = grafoDioses.inicio.obtener_elemento(origen)
#         for i in range(dios['aristas'].tamanio()):
#             nombre_dios = dios['aristas'].obtener_elemento(i)['destino']
#             dios_aux = dios['aristas'].obtener_elemento(i)['data']
#             if(len(dios_aux['relacion']) > 1):
#                 if(dios_aux['relacion'][1] == 'padre' or dios_aux['relacion'][1] == 'madre'):
#                     print(nombre_dios, dios_aux['relacion'])
#                     ancestro(nombre_dios)

# ancestro('Zeus')


# j. mostrar todos los nietos de Cronos;



# k. mostrar todos los hijos de Tea;