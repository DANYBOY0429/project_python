"""

   las listas nos permiten almacenar información en un lugar,
   la cantidad que se desee:ya sean pocos elementos o
   millones de elementos.


"""

bicycicles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycicles)


# como acceder a los elementos de una lista

"""
diciendole el indice de la lista, 
recordemos que el primer elemento de la lista 

"""

print(bicycicles[0])  # primer elemento
print(bicycicles[1])  # segundo elemento
print(bicycicles[2])  # tercer elemento 
print(bicycicles[3])  # cuarto elemento

print(bicycicles[-1])  # ultimo elemento
print(bicycicles[-2])  # penultimo elemento
print(bicycicles[0].upper())  # primer elemento en mayuscula
print(bicycicles[1].upper())  # segundo elemento en mayuscula
print(bicycicles[2].upper())  # tercer elemento en mayuscula
print(bicycicles[3].upper())  # cuarto elemento en mayuscula
message = f"My first bicycle was a {bicycicles[-1].upper()}."
print(message)
bicycicles.append('honda')  # agregando un elemento a la lista
print(bicycicles)
