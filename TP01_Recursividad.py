# Ejercicio 1
def fibonacci(numero):
    if (numero == 0 or numero == 1):
        return numero
    else:
        return fibonacci(numero-1)+fibonacci(numero-2)


# Ejercicio 2
# 3+2+1+0
# 3+sumatoria(2)
# 2+1+0
# 2+sumatoria(1)
# 1+0
def sumatoria(numero):
    if (numero == 0 ):
        return 0
    else:
        return numero+sumatoria(numero-1)


# Ejercicio 3
# (2*3)=6
# 2+(2*2)=6
# 2+(2*1)=4
# 2+(2*0)=2
def multiplicar(numero1,numero2):
    if(numero2 == 0):
        return 0
    else:
        return  numero1 + multiplicar(numero1,numero2-1)



# Ejercicio 4
# 4^2=16
# 4*(4^1)=16
# 4*(4^0)=4
def potencia(numero1,numero2):
    if (numero2 == 0 ):
        return 1
    else:
        return numero1 * potencia(numero1,numero2-1)




# Ejercicio 6

def invertir_cadena(cadena):
    if len(cadena) == 1 or len(cadena) == 0:
        return cadena
    else:
        print(cadena)
        return cadena[-1] + invertir_cadena(cadena[0:-1])


# print(invertir_cadena('salomon'))



# Ejercicio 7

def sumatoria_2(numero):
    if (numero == 1):
        return numero
    else:
        return 1/numero + sumatoria_2(numero-1)


# print(sumatoria_2(3))


# Ejercicio 10

def contador(numero, count):
    if count == len(str(numero)):
        return count
    else:
        return contador(numero,count+1)


# print(contador(1234567890,0))

# Ejercicio 14

def sumar_numeros(numero):
    if (numero == 0):
        return numero
    else:
        return (numero % 10) + sumar_numeros(numero // 10) 


# print(sumar_numeros(345))

###########################################################################################

# Ejercicio 5
def romano_a_decimal(letra):
    """Pasa una letra del sistema romano a su valor en sistema decimal"""
    if letra == "I":
        return 1
    elif letra == "V":
        return 5
    elif letra == "X":
        return 10
    elif letra == "L":
        return 50
    elif letra == "C":
        return 100
    elif letra == "D":
        return 500
    else:
        return 0

def convercion(numero):
    if len(numero) <= 1:
        return romano_a_decimal(numero)
    else:
        num_actual = romano_a_decimal(numero[0])
        num_siguiente = romano_a_decimal(numero[1])

        if num_actual >= num_siguiente:
            return  num_actual + convercion(numero[1:len(numero)])
        else:
            return convercion(numero[1:len(numero)]) - num_actual

# num = input("Ingresar numero romano: ")
# print("Resultado:", convercion(num))



# Ejercicio 8

def decimal_binario(numero):
    if numero == 0 or numero == 1:
        return str(numero)
    else:
        return decimal_binario(numero//2) + str(numero%2)

#print(decimal_binario(2))


# Ejercicio 22

def usar_la_fuerza(mochila):
    #if mochila == [] or mochila[objetos_sacados] == "Sable de luz" or len(mochila) - 1 == objetos_sacados:
    if mochila == [] or mochila[-1] == "Sable de luz":
        return mochila
    else:
        return usar_la_fuerza(mochila[0:-1])


mochila = ["Documento", "La sube" ,"Sable de luz", "Galletitas"]
# mochila = []

# num =len(mochila) - len(usar_la_fuerza(mochila))

# if num <= len(mochila) and num != 0:
#     print("El sable de luz está en la mochila")
# else:
#     print("El sable de luz no está en la mochila")

# print("Se sacaron", num, "objetos")


# Ejercicio 23

laberinto = [
    [1,0,1,0,0,0],
    [1,1,1,1,1,0],
    [1,0,1,0,1,0],
    [1,0,1,1,1,1],
    [1,1,1,0,0,1],
    [0,0,1,0,0,1],
    [1,1,1,1,1,1],
    [1,1,0,0,0,1],
]

def salir_del_laberinto(laberinto, x = 0, y = 0, camino = ""):
    # Pregunta si ya llego al final
    if x == len(laberinto) - 1 and y == len(laberinto[0]) -1:
        print("Camino: ", camino + "llegada")
        return True
    else:
        #pregunta si se esta analizando una posicion de la matriz valida
        if x < 0 or y < 0 or x > len(laberinto) -1 or y > len(laberinto[0]) -1:
            return False
        else:
            if laberinto[x][y] == 0:
                return False
            else:
                laberinto[x][y] = 0

                if salir_del_laberinto(laberinto, x + 1,y, camino + "v "):
                    return True
                elif salir_del_laberinto(laberinto, x, y+1, camino + "> "):
                    return True
                elif salir_del_laberinto(laberinto, x-1, y, camino + "^ "):
                    return True
                elif salir_del_laberinto(laberinto, x, y-1, camino + "< "):
                    return True
                else:
                    return False
                    
if not salir_del_laberinto(laberinto):
    print("No hay forma de salir del laberinto")

################################################################################



# Tomas Alaluf
# Gabriel Ramos
# Sebastian Maldonado
