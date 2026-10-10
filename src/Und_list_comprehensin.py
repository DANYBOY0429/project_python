"""
Una lista por comprensión es una forma concisa de crear listas 
en Python. Permite generar una nueva lista aplicando una 
expresión a cada elemento de una secuencia o iterable, 
opcionalmente filtrando elementos mediante una condición.
La sintaxis básica de una lista por comprensión es:         

"""



squares = [i**2 for i in range(1, 11)]
print(squares)  # imprime la lista con los primeros 10 numeros cuadraticos

students = ['ulisses', 'wendy', 'allison', 'abundis', 'danyboy']
# list comprehension con condicion
print("lista original de estudiantes:", students)
email_students = [student + "@upv.edu.mx" for student in students]
print("list comprehension:", email_students)  # imprime la lista con los estudiantes cuyo nombre tiene más de 4 caracteres

