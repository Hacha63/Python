#Colores
green = "\033[0;92m"
magenta = "\033[0;95m"
red = "\033[0;91m"

#Inicializar variables
va = 0
ve = 0
vi = 0
vo = 0
vu = 0
#Inicializo booleana
busca_vocal = True

#Introducción al programa
print(magenta + "Este programa cuenta cuantas veces sale cada vocal.\nIntrocuce letra a letra.\nIntroduce 0 para finalizar la secuencia.")

#while con la booleana para introducir valor
while busca_vocal == True:
            val1 = input(green + "Introduce una letra: ")

#if len para verificar que se introduce solo 1 letra y if para salir del bucle con 0
            if len(val1) <= 1:
                if val1 == "0":
                    busca_vocal = False
                else:
#Comparar el valor introducido con las diferentes vocales
                    if val1 == "A" or val1 == "a":
                        va = va + 1
                    if val1 == "E" or val1 == "e":
                        ve = ve + 1
                    if val1 == "I" or val1 == "i":
                        vi = vi + 1
                    if val1 == "O" or val1 == "o":
                        vo = vo + 1
                    if val1 == "U" or val1 == "u":
                        vu = vu + 1
            else:
                print(red + "Solo una letra")
#Fin de programa y mostrar resultados.
print(magenta + f"Aqui tienes la tabla con las veces que se han repetido las distintas vocales:\nA = {va}\nE = {ve}\nI = {vi}\nO = {vo}\nU = {vu}")