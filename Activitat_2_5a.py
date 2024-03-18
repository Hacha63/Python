#Colores
green = "\033[0;92m"
magenta = "\033[0;95m"
red = "\033[0;91m"

#Inicializo variables



#Control de errores para numero entero y entre 1-20
#def con nombre conterror sin variable porque nos introducen valores
def conterror():
    control = True
    while control == True:
        try:
            fact = int(input(green + "Introduce el valor para el calculo: "))
            if (1 <= fact <= 20):
                control = False
                return fact
            else:
               print(red + "El valor ha de ser un numero entero entre 1 y 20")
        except ValueError:
            print(red + "El valor ha de ser un numero entero entre 1 y 20")

#While para hacer la operacion factorial
#def con el nombre factorial con la variable (resultado1) que se podra reemplazar por el def del control de errores
def factorial(resultado1):
    resultado = 1
    cont = 1
    while cont <= resultado1:
        resultado = resultado * cont
        cont = cont + 1
        print(f"De momento el factorial és {resultado}")
    return resultado

#Explicación del programa
print(magenta + "Introduce un valor entero del cual quieras que se haga su calculo factorial.\nEl valor ha de ser entre 1 y 20, estos 2 incluidos.")


#Mostrar el resultado de la operacion
base = conterror()
print(magenta + f"El factorial de {base} és {factorial(base)}.")