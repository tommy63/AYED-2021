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