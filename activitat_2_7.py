#Toda la funcion def
def conterror():
    # Colores
    green = "\033[0;92m"
    magenta = "\033[0;95m"
    red = "\033[0;91m"

    #Inicializar variable de tabla y contador
    tab = [0,0,0,0]
    cont = 0
    #Explicacion
    print(magenta + f"Introduce 4 valores los cuales se ordenaran de menor a mayor. \nLos valores han de ser entre 0 y 1000")
    #Bucle para sacar 4 valores, esos 4 valores se introducen en la tabla usando la variable val
    #Los valores seran 0, 1, 2 pero esos numeros realmente seran la variable val cada vez que pase.
    while cont != 4:
        try:
            val = int(input(green + "Introduce un valor: "))
            if (1 <= val <= 1000):
                tab[cont] = val
                cont = cont + 1
            else:
               print(red + "El valor ha de ser entre 0 y 1000")
        except ValueError:
            print(red + "El valor ha de ser un numero entero")
    #Bucles par ordenar, usamos variable ordenar y con para ordenar los numeros dentro de la tabla
    ordenar = 0
    while ordenar < 3:
        con = 0
        while con < 3 - ordenar:
            if tab[con] > tab[con + 1]:
                tab[con], tab[con + 1] = tab[con + 1], tab[con]
            con = con + 1
        ordenar = ordenar + 1
    print(magenta + f"El orden de menor a mayor és:\n{tab}")

#Llamar toda la funcion def
conterror()