# Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
# nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
# ni métodos de ordenamiento.
from cola import Cola, barrido_cola

cola_a = Cola()
cola_b = Cola()
cola_combinada = Cola()
# [1, 2, 3, 4, 5, 11, 12, 13, 14, 15]
lista_a = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 22, 52]
lista_b = [8, 9, 10, 16, 17, 18, 19, 20, 29 ,48]

for i in lista_a:
    cola_a.arribo(i)
    # print("i>>> ", i)

for j in lista_b:
    cola_b.arribo(j)
    # print("j>>> ", j)

print("tamanio cola A: ", cola_a.tamanio())
print("tamanio cola B: ", cola_b.tamanio())

while not cola_a.cola_vacia() or not cola_b.cola_vacia():
    
    if cola_a.cola_vacia():
        cola_combinada.arribo(cola_b.atencion())
    
    elif cola_b.cola_vacia():
        cola_combinada.arribo(cola_a.atencion())
    
    else:
        if cola_a.en_frente() >= cola_b.en_frente():
            cola_combinada.arribo(cola_b.atencion())
        else:
            cola_combinada.arribo(cola_a.atencion())

barrido_cola(cola_combinada)