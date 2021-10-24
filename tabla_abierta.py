from lista import Lista

class TablaAbierta(object):
    def __init__(self, tamanio : int):
        self.__tamanio = tamanio
        self.__elementos : Lista = [None] * tamanio

    def insertar(self, hash, dato, clave = None, criterio=None):
        """Agrega un elemento a la tabla"""
        if clave:
            posicion = hash(clave, self.__tamanio)
        else:
            posicion = hash(dato, self.__tamanio)

        if(self.__elementos[posicion] is None):
            self.__elementos[posicion] = Lista()
        self.__elementos[posicion].insertar(dato, criterio)

    def eliminar(self, hash, dato,clave = None, criterio=None):
        """Elimina un elemento de la tabla y retorna dicho elemento"""
        if clave:
            posicion = hash(clave, self.__tamanio)
        else:
            posicion = hash(dato, self.__tamanio)

        if(self.__elementos[posicion] is not None):
            return self.__elementos[posicion].eliminar(dato, criterio)
        else:
            return None

    def buscar(self, hash, dato,clave = None, criterio=None):
        """Busca un elemento de la tabla y retorna dicho elemento"""
        if clave:
            posicion = hash(clave, self.__tamanio)
        else:
            posicion = hash(dato, self.__tamanio)

        if(self.__elementos[posicion] is not None):
            return self.__elementos[posicion].busqueda(dato, criterio)
        else:
            return None
