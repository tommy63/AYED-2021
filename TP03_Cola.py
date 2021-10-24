from cola import Cola

# Ejercicio 11



# Ejercicio 12



# Ejercicio 22

colaPersonajes = Cola()


class personaje(object):
        def __init__(self,nombre,heroe,sexo):
            self.nombre = nombre
            self.heroe = heroe
            self.sexo = sexo

        def __str__(self):
            return self.nombre+' - '+self.heroe+' - '+self.sexo
        
       






personajes = [
        personaje('Tony Stark','Iron Man','M'),
        personaje('Steve Rogers','Capitan America','M'),
        personaje('Natasha Romanoff','Blcak Widow','F'),
        personaje('Carol Danvers','Capitana Marvel','F'),
        personaje('Scott Lang','Ant Man','M'),
]

print('punto A')
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
for i in personajes:
        colaPersonajes.arribo(i)

cantida_elementos = 0
while cantida_elementos < colaPersonajes.tamanio():
        x = colaPersonajes.mover_final()
        if x.heroe == 'Capitana Marvel':
                print(x.nombre)          
        cantida_elementos += 1
print()
print('punto B')
# b. mostrar los nombre de los superhéroes femeninos;
cantida_elementos = 0
while cantida_elementos < colaPersonajes.tamanio():
        x = colaPersonajes.mover_final()
        if x.sexo == 'F':
                print(x.nombre)       
        cantida_elementos += 1
print()
print('punto C')
# c. mostrar los nombres de los personajes masculinos;
cantida_elementos = 0
while cantida_elementos < colaPersonajes.tamanio():
        x = colaPersonajes.mover_final()
        if x.sexo == 'M':
                print(x.nombre)      
        cantida_elementos += 1
print()
print('punto D')
# d. determinar el nombre del superhéroe del personaje Scott Lang;
cantida_elementos = 0
while cantida_elementos < colaPersonajes.tamanio():
        x = colaPersonajes.mover_final()
        if x.nombre == 'Scott Lang':
                print(x.heroe)     
        cantida_elementos += 1
print()
print('punto E')
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
cantida_elementos = 0
while cantida_elementos < colaPersonajes.tamanio():
        x = colaPersonajes.mover_final()
        if x.nombre[0] == 'S':
                print(x.nombre,x.heroe,x.sexo) 
        cantida_elementos += 1
print()
print('punto F')
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
cantida_elementos = 0
while cantida_elementos < colaPersonajes.tamanio():
        x = colaPersonajes.mover_final()
        if x.nombre== 'Carol Danvers':
                print(x.nombre,x.heroe)
        cantida_elementos += 1
