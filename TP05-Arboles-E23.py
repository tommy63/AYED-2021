import json
from arbol_binario import Arbol

def listadoInorden(arbol: Arbol):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            listadoInorden(arbol.izq)
        print("Criatura:", arbol.datos["Criatura"], ",",
              "Derrotado por:", arbol.datos["Derrotado"])
        if(arbol.der is not None):
            listadoInorden(arbol.der)

def cargarDescripcion(arbol : Arbol):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            cargarDescripcion(arbol.izq)
        arbol.datos["Descripcion"] = input(f"Descripcion para {arbol.info}: ")
        if(arbol.der is not None):
            cargarDescripcion(arbol.der)

#  Abrir archivo de craturas
archivo = open('criaturas.json', 'r')
contenido = archivo.read()
criaturas = json.loads(contenido)

arbolCriaturas = Arbol()

dic = {}

for criatura in criaturas:
    arbolCriaturas.insertar_nodo(criatura["Criatura"], criatura)

#  ejercicio 1
#  listadoInorden(arbolCriaturas)

#  ejercicio 2
#  cargarDescripcion(arbolCriaturas)

#  ejercicio 3
#  criatura = arbolCriaturas.busqueda('Talos')
#  print(criatura.datos)

#  ejercicio d
arbolCriaturas.balancear()
arbolCriaturas.conta_criaturas_derrotadas(dic)

print(dic)

archivo.close()
