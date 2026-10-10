"""
Tuplas---Inmutable---()
Listas---Mutables---[]

Las tuplas son listas que no cambian 
de tamaño, son inmutables.


"""

dimencions = (200,50)
print(dimencions)

# Como acceder a un elemento de una tabla

print("el largo de tu recatangulo es:", dimencions[0]) # imprime el largp
print("el ancho de tu rectangulo es:", dimencions[1]) # imprime el ancho

print(f"el largo de tu recatangulo es: {dimencions[0]}") # imprime el largp
print(f"el ancho de tu rectangulo es: {dimencions[1]}") # imprime el ancho


# Looping through tuple

for dimension in dimencions:
    print(dimencions)

names = ["dany","wendy","ulisses","allison","angel"]
print(names)
names[0]= "miguel"
print(names)



# truquillo - trick to change a tuple
dimencions = (1000,5000,2000)
print(dimencions)

anwer = False
print(anwer)


# TAREA ESTUDIAR EL METODO BUILD-IN DIRC()