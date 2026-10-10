# listas de numeros
"""
las listas pueden almacenar numeros.
las listas pueden almacenar numeros enteros, numeros   
flotantes y numeros complejos.

"""

# metodo build-in range() para crear listas de numeros enteros
number = range(1, 6)  # crea una lista de numeros enteros del 1 al 5
print(type(number))  # imprime el tipo de dato de la variable number


for value in range(0, 10):  # crea una lista de numeros enteros del 0 al 9
   
    print(value)  # imprime los numeros del 0 al 9

"""
el metodo build-in range() se utiliza para generar una 
secuencia de numeros enteros,el metodo build-in range()
puede recibir hasta 3 argumentos:
- start: el numero inicial de la secuencia (opcional, por 
defecto es 0
- stop: el numero final de la secuencia (obligatorio)
- step: el incremento entre cada numero de la secuencia 
(opcional, por defecto es 1)
"""
# crea una lista de utilizando  range

numbers = list(range(1, 11))  # crea una lista de numeros enteros del 1 al 10
print(numbers)  # imprime la lista de numeros enteros del 1 al 10

# lista con numeros pares del 2 al 10
even_numbers = list(range(0, 10, 2))  # crea una lista de numeros pares del 2 al 10
print(even_numbers)  # imprime la lista de numeros pares del 2 al 10

# lista con numeros impares del 1 al 19
odd_numbers = list(range(1, 20, 2))  # crea una lista de numeros impares del 1 al 19
print(odd_numbers)  # imprime la lista de numeros impares del 1 al 19

# la tabla del 7
table_7 = list(range(7, 71, 7))  # crea una lista con los múltiplos de 7 del 7 al 70
print(table_7)  # imprime la lista con los múltiplos de 7 del 7 al 70

# que pasa con un valor negativo en el metodo build-in range()
negative_range = list(range(-10, 0))  # crea una lista de numeros enteros negativos del -10 al -1
print(negative_range)  # imprime la lista de numeros enteros negativos del -10 al -1

