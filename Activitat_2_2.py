#Primero inicializo la variable num2 para usarla en el while de la linea 27
num2 = 1
#Variables de colores para que se vea bonito
green = "\033[0;92m"
magenta = "\033[0;95m"
red = "\033[0;91m"
#Introduzco un poco el programa
print(magenta + f"Introduce una secuencia de numeros entre 0 y 1000.\nIntroduce 0 para terminar la secuencia.\nSe mostrara el valor mas grande.\n")
#while True para control de caracteres con dentro un if para control de tamaño de numeros
while True:
    try:
        num1 = int(input(green + "Introduce el primer valor: "))
        if -1 <= num1 <= 1000:
            break
        else:
            print(red + "El numero ha de ser entre 0 y 1000")
    except ValueError:
        print(red + "El valor ha de ser un numero entero")

        continue
#if para comprobar si num1 no es 0 (fin de secuencia)
if num1 == 0:
    print(magenta + "En serio esa es tu secuencia? -_-")
else:
#while num2 no sea 0 (fin secuencia) dentro tiene el control de errores como num1
#if para ver que variable es más grande, si num2 es mas grande que num1, num1 tendra el valor de num2
    while num2 != 0:
        while True:
            try:
                num2 = int(input(green + "Introduce el siguiente valor: "))
                if -1 <= num2 <= 1000:
                    if num2 > num1:
                        num1 = num2
                    break
                else:
                    print(red + "El numero ha de ser entre 0 y 1000")
            except ValueError:
                print(red + "El valor ha de ser un numero entero")
#Una vez num2 es 0 se acaba la secuencia y muestro el numero mas grande (num1).
    print(magenta + f"El numero más alto de la secuencia és {num1}")