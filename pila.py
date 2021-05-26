
class Pila(object):
    
    def __init__(self):
        self.__elementos = []

    def apilar(self, dato):
        self.__elementos.append(dato)

    def desapilar(self):
        return self.__elementos.pop()
    
    def pila_vacia(self):
        return len(self.__elementos) == 0

    def tamanio(self):
        return len(self.__elementos)

    def elemento_cima(self):
        return self.__elementos[-1]

    def barrido_pila(self):
        aux = Pila()

        while not self.pila_vacia():
            num = self.desapilar()
            print(num)
            aux.apilar(num)

        while not aux.pila_vacia():
            self.apilar(aux.desapilar())

    def intercambiar_pila(pila : Pila):
        aux = Pila()

        while not pila.pila_vacia():
            aux.apilar(pila.desapilar())

        return aux

# from random import randint

# pila = Pila()
# pila_aux = Pila()

# for i in range(0, 10):
#     pila.apilar(randint(0, 100))

# print('cantidad de elementos', pila.tamanio())

# while(not pila.pila_vacia()):
#     x = pila.desapilar()
#     pila_aux.apilar(x)
#     print(x)

# print()
# while(not pila_aux.pila_vacia()):
#     x = pila_aux.desapilar()
#     pila.apilar(x)

# print()
# print(pila.tamanio())