#Importamos la libreria random
import  random

#Colores
green = "\033[0;92m"
magenta = "\033[0;95m"
red = "\033[0;91m"
print(magenta + "    __  ___           __                      _           __\n"
                "   /  |/  /___ ______/ /____  _________ ___  (_)___  ____/ /\n"
                "  / /|_/ / __ `/ ___/ __/ _ \/ ___/ __ `__ \/ / __ \/ __  /\n"
                " / /  / / /_/ (__  ) /_/  __/ /  / / / / / / / / / / /_/ /\n"
                "/_/  /_/\__,_/____/\__/\___/_/  /_/ /_/ /_/_/_/ /_/\__,_/\n")
#Def de control de errores
def conterror():
    control = True
    while control == True:
        try:
            val = int(input(green + "Introduce un valor: "))
            control = False
            return val
        except ValueError:
            print(red + "El valor ha de ser un numero entero")

#Especificar valor minimo
print(green + f"Valor minimo")
min = conterror()

#Especificar valor maximo
print(green + f"Valor maximo")
max = conterror()

#Variable de tabla (En linea porque soy un psicopata)
taula = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#Inicializo fila
fila = 0
#While para rellenar la tabla
while fila < 4:
    columna=0
    while columna < 4:
        #randint entre las 2 variables
        caracter = random.randint(min, max)
        taula[fila][columna]=caracter
        columna+=1
    fila+=1
fila=0
print(magenta + f"\nTabla:")
while fila < 4:
    print(f"{taula[fila]}")
    fila+=1