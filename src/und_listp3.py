print("aqui aprendia utilizar el metodo pop")
motorcycles_4 = ['honda', 'yamaha', 'suzuki', "mortalica"]
print(motorcycles_4)
deleted_motorcycle = motorcycles_4.pop()
print(f"tu mototocicleta borrada es: {deleted_motorcycle}")
print(motorcycles_4)


print("eliminar por indice")
motorcycles_5 = ['honda', 'yamaha', 'suzuki', "mortalica"]
print(motorcycles_5)
motorcycles_5.pop(1)  # eliminando el primer elemento de la lista
print(motorcycles_5)
print(motorcycles_5.pop(2))  # eliminando el cuarto elemento de la lista
print(motorcycles_5)



print("AQUI APRENDI A UTILIZAR EL METODO REMOVE")
motorcycles_6 = ['honda', 'yamaha', 'suzuki', "mortalica"]
print(motorcycles_6)
print(motorcycles_6.remove("mortalica"))  # eliminando un elemento por su valor
print(motorcycles_6)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()  # ordenando la lista alfabéticamente
print(cars)
print("ordenando la lista alfabéticamente en orden inverso")
cars.sort(reverse=True)  # ordenando la lista alfabéticamente en orden inverso
print(cars)

print("llevamos 5 metodos de las listas, append, insert, pop, remove y sort")

# TAREA estudiar el metodo de las listas .reverse()
"""
el metodo .reverse() invierte el orden de los elementos en la
lista, es decir, el primer elemento se convierte en el último 
y el último elemento se convierte en el primero. Este método 
modifica la lista original y no devuelve una nueva lista.
"""
print("AQUI APRENDI A UTILIZAR EL METODO REVERSE")
motorcycles_7 = ['honda', 'yamaha', 'suzuki', "mortalica"]
print(motorcycles_7)
motorcycles_7.reverse()
print(motorcycles_7)

# estudiar el metodos built-in de las listas .len() y el metodo .sorted() de las listas
# statement del .index()