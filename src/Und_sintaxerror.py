
# Eliminacion de espacios en blanco
programming_lenguage = "        Python        "
print(programming_lenguage)
print("Efecto del lstrip")
print(programming_lenguage.lstrip())
print(programming_lenguage.rstrip())
print(programming_lenguage.strip())

# Error de sntaxis

message = "una fortaleza de python es su comunidad"
print(message)
message = "una fortaleza de 'python' es su comunidad"
print(message)

# investigar que es el Zen de python 
"""
El Zen de Python es un conjunto de 19 principios que
influyen en el diseño del lenguaje de programación Python.
Fue escrito por Tim Peters y se puede acceder a él desde el 
intérprete de Python ejecutando el comando "import this".
Estos principios son considerados como una guía para escribir
código Python claro, legible y mantenible.
Estos son los 19 principios del Zen de Python:
beautiful is better than ugly.
explicit is better than implicit.
simple is better than complex.
complex is better than complicated.
flat is better than nested.
sparse is better than dense.
readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

bonito es mejor que feo.
explícito es mejor que implícito.
simple es mejor que complejo.
complejo es mejor que complicado.
plano es mejor que anidado.
escaso es mejor que denso.
la legibilidad cuenta.
Los casos especiales no son lo suficientemente 
especiales como para romper las reglas.
Aunque la practicidad vence a la pureza.
Los errores nunca deben pasar silenciosamente.
A menos que se silencien explícitamente.
Ante la ambigüedad, rechaza la tentación de adivinar.
debería haber una forma obvia de hacerlo.
Aunque esa forma puede no ser obvia al principio a menos 
que seas holandés.
Ahora es mejor que nunca.
Aunque nunca es a menudo mejor que *ahora* mismo.
Si la implementación es difícil de explicar, es una mala idea.
Si la implementación es fácil de explicar, puede ser una buena idea.
los espacios de nombres son una gran idea, ¡hagamos más de esos!.


"""