players = ["jason", "montes", "Charly", "wendy", "allison"]
print("lista original de jugadores:", players)


# slicing
print(players[3:5])  # Output: ['wendy', 'allison']

print(players[1:4])  # Output: ['montes', 'Charly', 'wendy']

print(players[0:3])  # Output: ['jason', 'montes', 'Charly']

print(players[2:5])  # Output: ['Charly', 'wendy', 'allison']

print(players[:3])  # Output: ['jason', 'montes', 'Charly']

print(players[-3:5])  # Output: ['Charly', 'wendy', 'allison']

print(players[0:-3])  # Output: ['jason', 'montes']

print(players[-4:-1])  # Output: ['montes', 'Charly', 'wendy']

"""
El slicing es una técnica que permite acceder a una porción de 
una lista, cadena o cualquier secuencia en Python. Se utiliza 
la sintaxis [inicio:fin] para obtener los elementos desde el 
índice 'inicio' hasta el índice 'fin - 1'. También se pueden 
usar índices negativos para contar desde el final de la 
secuencia.

"""

# Casos especiales de slicing
print("casos especiales de slicing".upper())
print(players)
print(players[1:10]) 
print(players[-10:10])
print(players[5:1])
print(players[:0])
print(players[0:1])

print("looping through the list".upper())
students = ["jason", "montes", "Charly", "wendy", "allison"]
for student in students[0:4]:
    print(f"el estudiante {student} paso la materia de python")


my_food = ["pizza", "hamburguesa", "hot dog", "tacos", "sushi"]


# tres maneras de copiar una lista

# 1. Usando slicing
my_food_copy1 = my_food[:]

# 2. Usando list()
my_food_copy2 = list(my_food)

# 3. Usando copy()
my_food_copy3 = my_food.copy()



