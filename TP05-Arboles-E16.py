#  Una empresa de nano satélites dedicada al monitoreo de lotes campo destinados al agro, tiene problemas para la transmisión de los datos recolectados, dado que la ventana de tiempo que dispone para enviar los datos antes de una nueva medición es muy corta, por lo que nos solicita desarrollar un algoritmo que permita comprimir la información para poder enviarla más rápi- do, para lo cual se debe tener en cuenta los siguientes requerimientos:

#  a.la información transmitida por el nano satélite son estado del tiempo, humedad del suelo, y tres dígitos que identifican el lote al cual pertenecen los datos;

#  b.desarrollar un árbol de Huffman que permita comprimir la información para transmitirla, la frecuencia de la información transmitida se observa en la siguiente tabla:

#  c.comprimir un mensaje y descomprimirlo, para ver si no se pierde información durante el
#  proceso de codificación, la trama enviada por el nano satélite tiene el siguiente formato
#  (estado del clima-humedad del suelo-cod1-cod2-cod3), por ejemplo la siguiente trama es
#  válida “Nublado-Baja-1-5-7”, –los guiones son a fines de comprender como está formada la
#  trama pero no forman parte de la misma–;
#  d.determinar la diferencia en tamaño de memoria utilizada por la trama original y la trama comprimida ­–puede utilizar la función getsizeof() de la librería sys–.

from sys import getsizeof
from arbol_binario import Arbol

def comparable(arbol : Arbol):
    return arbol.frecuencia

def generar_tabla(arbol,dic,cadena=''):
    if(arbol is not None):
        if(arbol.izq is None):
            dic[arbol.info] = cadena
        else:
            cadena += '0'
            generar_tabla(arbol.izq, dic, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(arbol.der, dic, cadena)

def codificar(variables, dic):
    cadena_cod = ''
    for variable in variables:
        cadena_cod += dic[variable]
    return cadena_cod
    
def decodificar(cadena_cod, arbol_huff):
    datos_deco = ''
    arbol_aux = arbol_huff
    pos = 0
    while(pos < len(cadena_cod)):
        if(cadena_cod[pos] == '0'):
            arbol_aux = arbol_aux.izq
        else:
            arbol_aux = arbol_aux.der
        pos += 1
        if(arbol_aux.izq is None):
            datos_deco += arbol_aux.info + '-'
            arbol_aux = arbol_huff

    return datos_deco[:-1]


#  Epieza el programa

dic = {}

tabla = [
    {"Simbolo" : "Despejado", "Frecuencia" : 0.22},
    {"Simbolo" : "Nublado", "Frecuencia" : 0.15},
    {"Simbolo" : "Lluvia", "Frecuencia" : 0.03},
    {"Simbolo" : "Baja", "Frecuencia" : 0.26},
    {"Simbolo" : "Alta", "Frecuencia" : 0.14},
    {"Simbolo" : "1", "Frecuencia" : 0.05},
    {"Simbolo" : "2", "Frecuencia" : 0.01},
    {"Simbolo" : "3", "Frecuencia" : 0.035},
    {"Simbolo" : "5", "Frecuencia" : 0.06},
    {"Simbolo" : "7", "Frecuencia" : 0.02},
    {"Simbolo" : "8", "Frecuencia" : 0.025}
]

bosque = []

#  generar bosque
for elemento in tabla:
    bosque.append(Arbol(info = elemento["Simbolo"], frecuencia=elemento["Frecuencia"]))

#  Ordenar bosque
bosque.sort(key=comparable)

#  generar arbol de huffman
while(len(bosque) > 1):
    arbol1 = bosque.pop(0)
    arbol2 = bosque.pop(0)
    nuevo_arbol = Arbol(frecuencia=arbol1.frecuencia+arbol2.frecuencia)
    nuevo_arbol.izq = arbol1
    nuevo_arbol.der = arbol2
    bosque.append(nuevo_arbol)
    bosque.sort(key=comparable)

arbol_huffman = bosque[0]

generar_tabla(arbol_huffman, dic)

mensajeParaCod = ['Nublado', 'Baja', '1', '2', '3']

mensjeCodificado = codificar(mensajeParaCod, dic)
estado_deco = decodificar(mensjeCodificado, arbol_huffman)

print('Estado original: ', mensajeParaCod);
print('Peso del estado sin codificar: ', getsizeof(mensajeParaCod))

print('Estado codificado: ', mensjeCodificado)
print('Peso de los datos codificado: ', getsizeof(mensjeCodificado))

print('\nEstado decodificado: ', estado_deco)
