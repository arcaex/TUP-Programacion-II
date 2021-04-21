# Leamos la cabecera del bucle como si de lenguaje natural se tratara:
# “para cada elemento en secuencia”. Y esto es exactamente lo que hace
# el bucle: para cada elemento que tengamos en la secuencia, ejecuta
# estas líneas de código.
# Lo que hace la cabecera del bucle es obtener el siguiente elemento de
# la secuencia secuencia y almacenarlo en una variable de nombre elemento. 
# Por esta razón en la primera iteración del bucle elemento valdrá
# “uno”, en la segunda “dos”, y en la tercera “tres”.

secuencia = [“uno”, “dos”, “tres”]
for elemento in secuencia:
    print elemento

# Como lo usaríamos en C
print("Numeros del 1 al 6")
for i in range(6):
    print(i)