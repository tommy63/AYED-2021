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

def ordenarPorDerrotado(dato):
    return dato[1]

def derrotadosPorHeracles(arbol : Arbol):
    if (arbol.info is not None):
        if (arbol.izq is not None):
            derrotadosPorHeracles(arbol.izq)
        if arbol.datos['Derrotado'] == 'Heracles':
            print(arbol.datos['Criatura'])
        if (arbol.der is not None):
            derrotadosPorHeracles(arbol.der)

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
# arbolCriaturas.balancear()
# arbolCriaturas.conta_criaturas_derrotadas(dic)
#
# lista_criaturas = []
#
# for key, value in dic.items():
#     temp = [key,value]
#     lista_criaturas.append(temp)
#
# lista_criaturas.sort(key=ordenarPorDerrotado)
#
# impresos = 0
# pos = len(lista_criaturas)
#
# print('Los tres heroes que derrotaron la mayor cantidad de criaturas son: ')
# while impresos < 3 and pos >= 0:
#     heroe = lista_criaturas[pos-1]
#     if heroe[0] != '-':
#         print(heroe[0])
#         impresos += 1
#     pos -= 1

# ejercicio e
# print('Papito heracles mato a todo esto bichos, un craaaaa')
# derrotadosPorHeracles(arbolCriaturas)

    

archivo.close()
