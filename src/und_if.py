# If Statement

print("aqui aprendi a usar el if".upper())

"""
Se utiliza un if para 

"""

cars = ["audi", "bmw", "toyota"]
for car in cars:
    if car == "audi":
        print(car.upper())
    else:
        print(car)       
print("-------------------------------------")
# El condicional es el corazon de un if

# condicional == para determinar igualdad
truk = "ford"
print(truk == "Ford".lower()) #true

# conditional false
print(truk == 'toyota') # false

# conditional != para determinar desigualdad
print(truk!='toyota') # true
print(truk!='ford') # false
print("-------------------------------------")
print('condicionales con numeros'.upper())
age = 17
print(age == 18) # false

anwer = 16
if anwer != 17:
    print('esa no es la respuesta correcta'.title())


print('condicional ulilizando >='.upper())

age = 18
print(age >= 18) # true

print('condicional ulilizando >'.upper())

print(age > 18) # false

print('condicional ulilizando <='.upper())

print(age <= 18) # true

print('condicional ulilizando <'.upper())

print(age < 18) # false

# > (mayor que)
# < (menor que)

# Operaciones boleanas
"""
AND, OR, NOT
 Y , O,   NO
 
|  A  |  B  | A & B |
|-------------------|
|  T    T       T   |
|  T    F       F   |




"""