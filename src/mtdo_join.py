#  Metodo join() de los strings

"""

 El método str.join(iterable) sirve para unir los elementos 
 de un iterable (lista, tupla, etc.) en una sola cadena,
 usando la cadena que llama al método como separado.
 
 separador: cadena que se colocará entre cada elemento.
 iterable: secuencia de cadenas (lista, tupla, 
 conjunto, etc.).
 Todos los elementos del iterable deben ser cadenas (str),
 si no, hay que convertirlos.

"""

# Unir con espacio

message = ("hola", "mundo", "python")
result = " " .join(message)
print(result)

result = "-" .join(message)
print(result)

result = "\n" .join(message)
print(result)

result= "\t" .join(message)
print(result)

"""
   join() no modifica la lista original,
   devuelve una nueva cadena.

   Es más eficiente que concatenar 
   en bucles con +.
   
   El separador puede ser cualquier cadena, 
   incluso vacía ("")

""" 
