#Variables de colores mas intuitivos.
green = "\033[0;92m"
magenta = "\033[0;95m"
red = "\033[0;91m"
#Inicializar variable cont para contar las veces que sale un numero
cont = 0
#Explicación
print(magenta + "Busca un numero en una secuencia introducida numero a numero.\nLos numeros han de ser entre 0 y 10000.\nIntroduce 0 para indicar el fin de la secuencia.")
#Inicializo la boleana para el numero a buscar
buscar_buscar = True
#Pregunto por numero para buscar + control de errores de entero y entre 0 y 10000
while buscar_buscar == True:
    try:
        buscar = int(input(green + "Introduce el valor a buscar: "))
        if (0 < buscar <= 10000) and (buscar != 0):
            buscar_buscar = False
        else:
            print(red + "El valor ha de ser un numero entero entre 0 y 10.000")
    except ValueError:
        print(red + "El valor ha de ser un numero entero entre 0 y 10.000")
#Inicializo la boleana para la secuencia
buscar_secuencia = True
#Pregunto por numero de secuencia + control de errores de entero y entre 0 y 10000
while buscar_secuencia == True:
    try:
        secuencia = int(input(green + "Introduce un numero de la secuencia: "))
        if secuencia == 0:
            buscar_secuencia = False
        if (0 < secuencia <= 10000) and (secuencia != 0):
            if secuencia == buscar:
                cont = cont + 1
    except ValueError:
        print(red + "El valor ha de ser un numero entero entre 0 y 10.000")
#Muestro el resultado
print(magenta + f"**********************************\nEl numero {buscar} se repite {cont} veces.\n**********************************")