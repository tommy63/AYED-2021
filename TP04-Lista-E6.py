from lista import Lista, quicksort

# Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:

# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

listaSuperheroes = Lista()
sublistaSuperheroes = Lista()

superheroes = [
    {"nombre" : "Wolverine", "anio" : 1998, "casa" : "DC", "biografia" : "Tiene armadura"},
    {"nombre" : "Linterna Verde", "anio" : 1960, "casa" : "MARVEL", "biografia" : "asddfdds"},
    {"nombre" : "Dr. Strange", "anio" : 1955, "casa" : "DC", "biografia" : "traje"},
    {"nombre" : "Bbn", "anio" : 1955, "casa" : "MARVEL", "biografia" : "asddfdds"}
]

for superheroe in superheroes:
    listaSuperheroes.insertar(superheroe, 'nombre')

# Eliminar el nodo que contiene la información de Linterna Verde
listaSuperheroes.eliminar('Linterna Verde', 'nombre')

# b. mostrar el año de aparición de Wolverine;
pos = listaSuperheroes.busqueda("Wolverine", "nombre")
print(listaSuperheroes.obtener_elemento(pos)["anio"])

# c. cambiar la casa de Dr. Strange a Marvel;
pos = listaSuperheroes.busqueda("Dr. Strange", "nombre")

if pos > -1:
    # superheroe = listaSuperheroes.eliminar("Dr. Strange", "nombre")
    # superheroe["casa"] = "MARVEL"
    # listaSuperheroes.insertar(superheroe,"nombre")

    # superheroe = listaSuperheroes.obtener_elemento(pos)
    # superheroe["casa"] = "MARVEL"
    # listaSuperheroes.modificar_elemento(pos, superheroe, "nombre")

    listaSuperheroes.obtener_elemento(pos)["casa"] = "MARVEL"

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
for i in range(listaSuperheroes.tamanio()):
    superheroe = listaSuperheroes.obtener_elemento(i)

    if "armadura" in superheroe["biografia"] or "traje" in superheroe["biografia"]:
        print(superheroe["nombre"])

# mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
for i in range(listaSuperheroes.tamanio()):
    superheroe = listaSuperheroes.obtener_elemento(i)

    if superheroe['anio'] < 1963:
        print(superheroe["nombre"], superheroe["casa"])

# h. listar los superhéroes que comienzan con la letra B, M y S;
for i in range(listaSuperheroes.tamanio()):
    superheroe = listaSuperheroes.obtener_elemento(i)

    if superheroe['nombre'][0] in ["B", "M", "S"]:
        sublistaSuperheroes.insertar(superheroe, "nombre")

print("Sublista")
sublistaSuperheroes.barrido()
