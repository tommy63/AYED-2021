from arbol_binario import Arbol
from random import randint

#  El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
#  resolver los siguientes requerimientos:

def infoTrex(arbol : Arbol):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            infoTrex(arbol.izq)
        if(arbol.datos[0] == 'T-Rex'):
            print(arbol.datos)
        if(arbol.der is not None):
            infoTrex(arbol.der)

def ubicacionRaptor(arbol : Arbol):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            ubicacionRaptor(arbol.izq)
        if(arbol.datos[0] == 'Raptor'):
            print(arbol.datos[2])
        if(arbol.der is not None):
            ubicacionRaptor(arbol.der)

def cambioNombre(arbol : Arbol):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            cambioNombre(arbol.izq)
        if(arbol.datos[0] == 'Sgimoloch'):
            print(arbol.datos[0] == 'Stygimoloch')
        if(arbol.der is not None):
            cambioNombre(arbol.der)


#  1. almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
#  conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter
#  por ejemplo 7A), existen varios dinosaurios con el mismo nombre pero sus códigos son
#  distintos, los códigos no pueden ser repetidos (tenga cuidado);

dinosaurios = [
    ['T-Rex', 1, str(randint(0,9)) + chr(randint(65, 91))],
    ['T-Rex', 2, str(randint(0,9)) + chr(randint(65, 91))],
    ['T-Rex', 20, str(randint(0,9)) + chr(randint(65, 91))],
    ['Diplodocus', 5, str(randint(0,9)) + chr(randint(65, 91))],
    ['Sgimoloch', 12, str(randint(0,9)) + chr(randint(65, 91))],
    ['Diplodocus', 6, str(randint(0,9)) + chr(randint(65, 91))],
    ['Sgimoloch', 10, str(randint(0,9)) + chr(randint(65, 91))],
    ['T-Rex', 11, str(randint(0,9)) + chr(randint(65, 91))],
    ['Raptor', 792, str(randint(0,9)) + chr(randint(65, 91))],
    ['T-Rex', 4, str(randint(0,9)) + chr(randint(65, 91))],
    ['Raptor', 14, str(randint(0,9)) + chr(randint(65, 91))],
    ['Raptor', 16, str(randint(0,9)) + chr(randint(65, 91))],
    ['Sgimoloch', 7, str(randint(0,9)) + chr(randint(65, 91))],
    ['Sgimoloch', 17, str(randint(0,9)) + chr(randint(65, 91))],
    ['Raptor', 15, str(randint(0,9)) + chr(randint(65, 91))],
    ['Raptor', 13, str(randint(0,9)) + chr(randint(65, 91))]
]


#  2. se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por
#  código;
arbolNombre = Arbol()
arbolCodigo = Arbol()
for dinosaurio in dinosaurios:
    arbolNombre.insertar_nodo(dinosaurio[0], dinosaurio)
    arbolCodigo.insertar_nodo(dinosaurio[1], dinosaurio)

#  3. realizar un barrido en orden del árbol ordenado por nombre;
#  arbolNombre.inorden()




#  4. mostrar toda la información del dinosaurio 792;
#  dinosaurio = arbolCodigo.busqueda(792)
#  if dinosaurio:
    #  print(dinosaurio.datos)




#  5. mostrar toda la información de todos los T-Rex que hay en la isla;
#  infoTrex(arbolNombre)




#  6. modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
#  cargado, su nombre correcto es Stygimoloch;
#  cambioNombre(arbolNombre)
#  cambioNombre(arbolCodigo)
#  arbolCodigo.inorden()
#  arbolNombre.inorden()




#  7. mostrar la ubicación de todos los Raptores que hay en la isla;
#  ubicacionRaptor(arbolNombre)




#  8. contar cuantos Diplodocus hay en el parque;
#  cant = arbolNombre.contar_ocurrencias('Diplodocus')
#  print('Cantidad:', cant)


