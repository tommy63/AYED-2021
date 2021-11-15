#  16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
#  siguiente situación:
#  a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
#  b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
#  c. cargue dos documentos del staff de TI.
#  d. cargue un documento del gerente.
#  e. imprima los dos primeros documentos de la cola.
#  f. cargue dos documentos de empleados y uno de gerente.
#  g. imprima todos los documentos de la cola de impresión.

from heap import HeapMin, HeapMax

def barridoColaPrioridad(cola):
    for i in range(cola.tamanio):
        print(cola.atencion())

documentos = [
    [ 3, 'Documento gerent' ],
    [ 1, 'memes' ],
    [ 2, 'Documentacion' ]
]

colaImpresion = HeapMax()

#  a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
for doc in documentos:
    colaImpresion.arribo(doc[1], doc[0])

#  b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
#  print(colaImpresion.atencion())

#  c. cargue dos documentos del staff de TI.
#  colaImpresion.arribo('ghaka', 2)
#  colaImpresion.arribo('sdasddfa', 2)
#  colaImpresion.monticulizar(colaImpresion.elementos)
#  barridoColaPrioridad(colaImpresion)

#  d. cargue un documento del gerente.
#  colaImpresion.arribo('Manaos', 3)
#  colaImpresion.monticulizar(colaImpresion.elementos)
#  barridoColaPrioridad(colaImpresion)

#  e. imprima los dos primeros documentos de la cola.
#  print(colaImpresion.atencion())
#  print(colaImpresion.atencion())

#  f. cargue dos documentos de empleados y uno de gerente.
#  colaImpresion.arribo('ghaka', 1)
#  colaImpresion.arribo('sdasddfa', 1)
#  colaImpresion.arribo('sdasddfa', 3)
#  colaImpresion.monticulizar(colaImpresion.elementos)
#  barridoColaPrioridad(colaImpresion)

#  g. imprima todos los documentos de la cola de impresión.
#  barridoColaPrioridad(colaImpresion)
