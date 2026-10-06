#  TAREA estudiar el metodo de las listas .reverse()
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
"""
El método built-in len() devuelve el número de elementos en 
una lista, mientras que el método sorted() devuelve una nueva 
lista ordenada sin modificar la lista original.
"""
print("AQUI APRENDI A UTILIZAR EL METODO LEN()")
motorcycles_8 = ['honda', 'yamaha', 'suzuki', "mortalica"]
print(len(motorcycles_8))  # devuelve el número de elementos en la lista


print("AQUI APRENDI A UTILIZAR EL METODO SORTED()")
motorcycles_9 = ['honda', 'yamaha', 'suzuki', "mortalica"]
print(sorted(motorcycles_9))  # devuelve una nueva lista ordenada
print(motorcycles_9)  # la lista original no se modifica
print(sorted(motorcycles_9, reverse=True))  # devuelve una nueva lista ordenada en orden inverso
print(motorcycles_9)  # la lista original no se modifica



# statement del .index()

"""
El método .index() devuelve el índice del primer elemento
encontrado en la lista que coincide con el valor especificado.
"""
print("AQUI APRENDI A UTILIZAR EL METODO INDEX()")
motorcycles_10 = ['honda', 'yamaha', 'suzuki', "mortalica"]
print(motorcycles_10.index('suzuki'))  # devuelve el índice del primer elemento encontrado en la lista que coincide con el valor especificado
print(motorcycles_10.index('honda'))  # devuelve el índice del primer elemento encontrado en la lista que coincide con el valor especificado
print(motorcycles_10.index('mortalica'))  # devuelve el índice del primer elemento encontrado en la lista que coincide con el valor especificado
print(motorcycles_10.index('yamaha'))  # devuelve el índice del primer elemento encontrado en la lista que coincide con el valor especificado


print("El dia de hoy voy a aprender a trabajar con las listas .upper)")
magicians = [ "ronaldinho", "messi", "neymar", "cristiano", "pele", "maradona"]
print(magicians)

print("imprimir ala la mala")
print(magicians[0], magicians[1], magicians[2], magicians[3], magicians[4], magicians[5])
print("imprimir con un for")
for magician in magicians:
    print(magician, end=" ")
    print()
    print(magician)
    print(magician.title())
    print(magician.upper())
    print(magician.lower())




"""
for-aux-in-iter
A esto se le conoce como loping, es decir, repetir un 
bloque de código varias veces.

"""



# identacion 
"""
python utiliza la identación para definir bloques de código.
La identación es el espacio en blanco al principio de una línea
de código.
se utilizan 4 espacios en blanco para la identación.
"""
# no olvidemos identar - traceback indentacionerror

magicians = [ "ronaldinho", "messi", "neymar", "cristiano", "pele", "maradona"]
for magician in magicians:
    print(magician)

# error de logica - logic error

for magician in magicians:
    print(magician)
    print(f"no pudo esperar a ver el siguiente truco") 

# identacion innesesaria - unnecessary indentation
message = "hello"
print(message)  # esto genera un error de identación innecesaria

for magician in magicians:
    print(magician)  # esto genera un error de identación innecesaria

