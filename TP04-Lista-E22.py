from lista import Lista, quicksort

# Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos:
# nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recaudacion. Desarrolle los algoritmos necesarios para realizar las siguientes tareas:

# a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado año–;
# b. mostrar los datos de la película que más recaudo;
# c. indicar las películas con mayor valoración del público, puede ser más de una;
# d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una lista auxiliar–:
#   I. por nombre,
#   II. por recaudacion,
#   III. por año de estreno,
#   IV. por valoración del público.

def ordenar(lista : Lista, criterio : str):
    """Crea y carga una lista auxiliar con los valores de la lista recibida segun el criterio y retorna la lista auxiliar"""
    aux = Lista()
    for i in range(lista.tamanio()):
        aux.insertar(lista.obtener_elemento(i), criterio)
    return aux

def mostrar_por_anio(lista : Lista, anio : int):
    """Muestra todas las peliculas estrenada en determinado anio"""
    for i in range(lista.tamanio()):
        pelicula = lista.obtener_elemento(i)
        if pelicula['anioEstreno'] == anio: 
            print(pelicula)
    
listaPeliculas = Lista()

peliculas = [
    { 'nombre' : 'Star Wars: Episodio I - La amenaza fantasma', 'valPublico' : 8, 'anioEstreno' : 1999, 'recaudacion' : 1010 },
    { 'nombre' : 'Star Wars: Episodio II - El ataque de los clones', 'valPublico' : 7, 'anioEstreno' : 2002, 'recaudacion' : 2540 },
    { 'nombre' : 'Star Wars: Episodio V - El Imperio contraataca', 'valPublico' : 5, 'anioEstreno' : 1986, 'recaudacion' : 26625 },
    { 'nombre' : 'Star Wars: Episodio VII - El despertar de la Fuerza', 'valPublico' : 9, 'anioEstreno' : 1993, 'recaudacion' : 6377 },
    { 'nombre' : 'Star Wars: Episodio VIII - Los últimos Jedi', 'valPublico' : 8, 'anioEstreno' : 2017, 'recaudacion' : 500 }
]

# Insertar las peliculas en la lista
for pelicula in peliculas:
    listaPeliculas.insertar(pelicula, 'nombre')

# A
anio = 2002 or int(input("Ingresar anio: "))
print(f'Peliculas estrenadas en el anio {anio}')
mostrar_por_anio(listaPeliculas, anio)
print()
#B
print('Pelicula o peliculas de mayor recaudacion')
listaPeliculas.ordenar('recaudacion')
i = listaPeliculas.tamanio() - 1
mayor = listaPeliculas.obtener_elemento(i)['recaudacion']

while i >= 0 and listaPeliculas.obtener_elemento(i)['recaudacion'] == mayor:
    print(listaPeliculas.obtener_elemento(i))
    i -= 1

print()
#C

print('Pelicula o peliculas de mejor valoracion del publico')
listaPeliculas.ordenar('valPublico')
i = listaPeliculas.tamanio() - 1
mayor = listaPeliculas.obtener_elemento(i)['valPublico']

while i >= 0 and listaPeliculas.obtener_elemento(i)['valPublico'] == mayor:
    print(listaPeliculas.obtener_elemento(i))
    i -= 1
print()

#D
print('Lista de peliculas ordenadas por nombre')
listaPeliculas.ordenar('nombre')
listaPeliculas.barrido()
print()

print('Lista de peliculas ordenadas por recaudacion')
listaPeliculas.ordenar('recaudacion')
listaPeliculas.barrido()
print()


print('Lista de peliculas ordenadas por valoracion del anio de estreno')
listaPeliculas.ordenar('anioEstreno')
listaPeliculas.barrido()
print()

print('Lista de peliculas ordenadas por valoracion del publico')
listaPeliculas.ordenar('valPublico')
listaPeliculas.barrido()
print()
