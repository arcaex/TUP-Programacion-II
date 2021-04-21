# El bucle while (mientras) ejecuta un fragmento de código mientras se
# cumpla una condición.

edad = 0
while edad < 18:
    edad = edad + 1
    print “Felicidades, tienes “ + str(edad)

salir = False
while not salir:
    entrada = raw_input()
    if entrada == “adios”:
    salir = True
    else:
    print entrada