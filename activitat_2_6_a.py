
def conterror():
    # Colores
    green = "\033[0;92m"
    magenta = "\033[0;95m"
    red = "\033[0;91m"

    #Inicializar variable de tabla y contador
    tab = [0,0,0]
    cont = 0

    #Bucle para sacar 3 valores, esos 3 valores se introducen en la tabla usando los valores de la variable cont
    #Los valores seran 0, 1, 2 pero esos numeros realmente seran la variable val cada vez que pase.
    while cont != 3:
        try:
            val = int(input(green + "Introduce un valor: "))
            if (1 <= val <= 1000):
                tab[cont] = val
                cont = cont + 1
            else:
               print(red + "El valor ha de ser entre 1 y 1000")
        except ValueError:
            print(red + "El valor ha de ser un numero entero")

#Comparando tamaños, usando 0, 1, 2 de la tabla que realmente són los valores introducidos de la variable val
    if tab[0] > tab[1]:
        tab[0], tab[1] = tab[1], tab[0]
    if tab[1] > tab[2]:
        tab[1], tab[2] = tab[2], tab[1]
    if tab[0] > tab[1]:
        tab[0], tab[1] = tab[1], tab[0]

#Se muestra el resultado de la tabla ya ordenada
    print(magenta + f"El orden és: {tab}")

#Llamamos al def
conterror()
