# Daniel Rodriguez Moreno

# 2630303

# Grupo 3

# PRINCIPIOS Y BUENAS PRÁCTICAS
"""
- Los strings son inmutables: cualquier cambio genera una 
nueva cadena.
- Es buena práctica normalizar entrada con strip() y lower() 
antes de compararla.
- Evitar "números mágicos" en índices; documentar qué extrae 
cada slice.
- Usar métodos de string en lugar de reescribir lógica básica.
- Diseñar validaciones claras: primero que no esté vacío, luego 
el formato.
- Escribir código legible: nombres de variables claros y 
mensajes de error entendibles.
"""
# Resumen ejecutivo

"""
un string en Python es un tipo de dato que representa una 
secuencia de caracteres. Los strings son inmutables, lo que 
significa que una vez creados, no se pueden modificar 
directamente; cualquier operación que parezca modificar un 
string en realidad crea uno nuevo.
Es importante validar y normalizar texto de entrada para 
asegurar que los datos sean consistentes y seguros, especialmente
en aplicaciones que manejan información sensible como correos.


- ¿Qué cubrirá tu documento?: descripción de cada problema, 
diseño de entradas y salidas, validaciones aplicadas y uso de 
métodos de string con casos de prueba (incluyendo el código).

"""

# Problems

 # Problem 1: Full name formatter
"""
    Description: Este problema consiste en tomar un nombre 
    completo ingresado por el usuario y formatearlo de manera 
    adecuada, asegurando que cada parte del nombre comience con 
    una letra mayúscula y que no haya espacios innecesarios.

    input:
    full_name: string - El nombre completo ingresado por el 
    usuario(puede ser con mayusculas, minusculas o espacios).
    
    output:
    full_name_formatted: string - El nombre completo 
    formateado de manera adecuada, con la primera letra de 
    cada palabra en(mayúscula/m minuscula) sin espacios 
    innecesarios.
   
    Validations:
    - El nombre completo no debe estar vacío.
    - El nombre completo debe contener al menos un carácter
    - El nombre completo debe contener solo letras y espacios.
"""
# TEST CASES:
print("formatter".upper())

    # Normal case:
full_name = "  daniel rodrigues moreno  "
print(full_name.strip().title())  # Output: "Daniel Rodrigues Moreno"

    # Border case:
full_name = "a"
print(full_name.strip().title())  # Output: "A" 

    # Error case:
full_name = "1234"
if not full_name.strip().isalpha():
    print("Error: El nombre completo debe contener solo letras y espacios.")  # Output: Error message


 # problem 2: Email validator

"""
    Description: Este problema consiste en validar una 
    dirección de correo electrónico ingresada por el usuario, 
    asegurando que cumpla con un formato básico de correo 
    electrónico.

    input:
    email: string - La dirección de correo electrónico 
    ingresada por el usuario.

    output:
    is_valid: boolean - True si el correo electrónico es válido,
    False en caso contrario.

    Validations:
    - El correo electrónico no debe estar vacío.
    - El correo electrónico debe contener un "@" y un ".".
    - El correo electrónico debe tener al menos un carácter
    antes del "@" y al menos un carácter entre el "@" y el ".".

"""
# TEST CASES:
print("email")

    # Normal case:
email = "danielrodrigues@example.com"
print(email.strip().count("@") == 1 and email.strip().count(".") >= 1 and email.strip().find("@") > 0 and email.strip().find(".") > email.strip().find("@"))  # Output: True

    # Border case:
email = "a@b.m"
print(email.strip().count("@") == 1 and email.strip().count(".") >= 1 and email.strip().find("@") > 0 and email.strip().find(".") > email.strip().find("@"))  # Output: True

    # Error case:
email = "invalid-email"
print(email.strip().count("@") == 1 and email.strip().count(".") >= 1 and email.strip().find("@") > 0 and email.strip().find(".") > email.strip().find("@"))  # Output: False


 #problem 3: Palindrome checker 

"""
    Description: Este problema consiste en verificar si una
    cadena de texto ingresada por el usuario es un palíndromo,
    es decir, si se lee igual de izquierda a derecha que de
    derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.
    
    input:
    text: string - La cadena de texto ingresada por el usuario.

    output:
    is_palindrome: True si la cadena es un palíndromo,
    False en caso contrario.

    Validation: phrase no vacía tras strip().
    Longitud mínima razonable después de limpiar espacios 
    (por ejemplo, al menos 3 caracteres).



"""
# TEST CASES:
print('palindromos'.upper())
   
    # Normal case:

def is_a_palíndromo(texto): return texto == texto[::-1]
print(is_a_palíndromo("level")) # true

    # Border case:

def is_a_palíndromo(texto): return texto == texto[::-1]
print(is_a_palíndromo("a")) # true

    # Error case:

def is_a_palíndromo(texto): return texto == texto[::-1]
print(is_a_palíndromo("cakes")) # false



 #problem 4: Sentence word stats 
"""
    Description:
    Dada una oración, se debe normalizar el texto,
    organizarze, eliminar espacios al inicio y al
    final y separar por espacios.
    Tambien debe arrojar el numero de palabras,
    la primera y la ultima palabra y al igual que la 
    palabra mas larga por longitud.

    input:

    outpot:

    validations:
    
"""

 #problem 5: Password strength classifier

 #problem 6: Product label formatter
 

# Conclusiones
# Referencias (mínimo 5)
"""
https://docs.python.org/es/3/library/string.html#module-string
https://www.geeksforgeeks.org/python/why-are-python-strings-immutable/


"""