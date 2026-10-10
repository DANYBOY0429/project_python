"""
crear una unna lista con
los primertos 10 numeros cuadraticos
"""
squares = []
for value in range(1, 11):
    square = value ** 2
    print(f"el valor que voy a agregar a la lista es: {square}")
    squares.append(square)
print(squares)  # imprime la lista con los primeros 10 numeros cuadraticos



quadratic_numbers = [i**2 for i in range(1, 11)]
print(quadratic_numbers)  # imprime la lista con los primeros 10 numeros cuadraticos

# list comprehension con 
"""
las list comprehension es una forma concisa de crear listas en 
Python.
Permite generar una nueva lista aplicando una expresión a cada 
elemento de una secuencia o iterable, todo en una sola línea de 
código.
La sintaxis básica de una list comprehension es: 

"""