import json
from arbol_binario import Arbol
from cola import Cola

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

def noFueronDerrotados(arbol : Arbol, lista):
    if (arbol.info is not None):
        if (arbol.izq is not None):
            noFueronDerrotados(arbol.izq, lista)
        if arbol.datos['Derrotado'] == '-':
            lista.append(arbol.datos['Criatura'])
        if (arbol.der is not None):
            noFueronDerrotados(arbol.der, lista)

def agregarCapturada(arbol : Arbol):
    if (arbol.info is not None):
        if (arbol.izq is not None):
            agregarCapturada(arbol.izq)
        arbol.datos['Capturada'] = input(f'Agregar heroe que capturo a {arbol.info}: ')
        if (arbol.der is not None):
            agregarCapturada(arbol.der)

def capturadoPorHeracles(arbol : Arbol):
    if (arbol.info is not None):
        if (arbol.izq is not None):
            capturadoPorHeracles(arbol.izq)
        if arbol.datos['Capturada'] == 'Heracles':
            print(arbol.datos['Criatura'])
        if (arbol.der is not None):
            capturadoPorHeracles(arbol.der)


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

# ejercicio f

# lista_derrotados = []
#
# noFueronDerrotados(arbolCriaturas,lista_derrotados)
# print(lista_derrotados)

# ejercicio g
# agregarCapturada(arbolCriaturas)
# arbolCriaturas.inorden()

# ejercicio h
# lista_heracles = ['Cerbero', 'Toro de Creta', 'Cierva Cerinea', 'Jabalí de Erimanto']
#
# for criatura in lista_heracles:
#     criaturaEncontrada = arbolCriaturas.busqueda(criatura)
#     if criaturaEncontrada:
#         criaturaEncontrada.datos['Capturada'] = 'Heracles'
#
# arbolCriaturas.inorden()


# ejercicio i
# arbolCriaturas.busqueda_proximidad('la')


#ejercicio j
# arbolCriaturas.inorden()
# print()
# arbolCriaturas.eliminar_nodo('Basilisco')
# arbolCriaturas.eliminar_nodo('Sirenas')
# arbolCriaturas.inorden()

# ejercicio k
# criaturaEncontrada = arbolCriaturas.busqueda('Aves del Estinfalo')
# if criaturaEncontrada:
#     criaturaEncontrada.datos['Cant_Derrotado'] = 5
#     print(criaturaEncontrada.datos)

# ejercicio l
# criaturaEncontrada = arbolCriaturas.busqueda('Ladon')
# if criaturaEncontrada:
#     criaturaEncontrada.datos['Criatura'] = 'Dragon Ladon'
#     print(criaturaEncontrada.datos)

# ejercicio m
# arbolCriaturas.barrido_por_nivel()

# ejercicio n


# print('Papito heracles capturo a todo esto bichos, un craaaaaaaaaa')
# capturadoPorHeracles(arbolCriaturas)

archivo.close()
