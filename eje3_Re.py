
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


# Ejercicio 5
# 4=IV
# 1-5=4
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


print(sumar_numeros(345))

