#Colores
green = "\033[0;92m"
magenta = "\033[0;95m"
red = "\033[0;91m"

#Inicializo variables
resultado = 1
cont = 1
control = True

#Explicación del programa
print(magenta + "Introduce un valor entero del cual quieras que se haga su calculo factorial.\nEl valor ha de ser entre 1 y 20, estos 2 incluidos.")

#Control de errores para numero entero y entre 1-20
while control == True:
    try:
        fact = int(input(green + "Introduce el valor para el calculo: "))
        if (1 <= fact <= 20):
            control = False
        else:
            print(red + "El valor ha de ser un numero entero entre 1 y 20")
    except ValueError:
        print(red + "El valor ha de ser un numero entero entre 1 y 20")

#While para hacer la operacion factorial
while cont <= fact:
    resultado = resultado * cont
    cont = cont + 1
    print(f"De momento el factorial és {resultado}")

#Mostrar el resultado de la operacion
print(magenta + f"El factorial de {fact} és {resultado}.")