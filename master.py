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

def jugadores():
    control = True
    print(magenta + "    o     |    o   o \n"
                    "   /|\    |   /|\ /|\ \n"
                    "   / \    |   / \ / \ \n"
                    "    1     |      2   \n")

    while control == True:
        try:
            jugadores = int(input(green + "Selecciona 1 o 2 dependiendo con el numero de jugadores: "))
            if (jugadores == 1 or jugadores == 2):
                control = False
                return jugadores
            else:
                print(red + "Elije entre 1 y 2 jugadores.")
        except ValueError:
            print(red + "El valor ha de ser o 1 o 2.")


def dif():
    control = True
    print(green + ".----.  .--.   .----..-.  .-.    .-. .-. .---. .---. .-.  .-.  .--.  .-.       .-. .-.  .--.  .---. .----.\n"
                  "} |__} / {} \ { {__-` \ \/ /     |  \{ |/ {-. \} }}_}}  \/  { / {} \ } |       { {_} | / {} \ } }}_}} {-. \ \n"
                  "} '__}/  /\  \.-._} }  `-\ }     | }\  {\ '-} /| } \ | {  } |/  /\  \} '--.    | { } }/  /\  \| } \ } '-} / \n"
                  "`----'`-'  `-'`----'     `-'     `-' `-' `---' `-'-' `-'  `-'`-'  `-'`----'    `-' `-'`-'  `-'`-'-' `----' \n"
                  "             1.                                      2.                                     3.\n")
    while control == True:
        try:
            dif = int(input(green + "Selecciona la dificultad con 1, 2 o 3: "))
            if (1 <= dif <= 3):
                control = False
                return dif
            else:
                print(red + "Elije entre 1, 2 o 3.")
        except ValueError:
            print(red + "El valor ha de ser 1, 2 o 3.")

personas = jugadores()
print(magenta + f"{personas} jugadores seleccionado")

dificultad = dif()


if dificultad == 1:
    print(green + "Has seleccionado la dificutlad:\n"
                  ".----.  .--.   .----..-.  .-.\n"
                  "} |__} / {} \ { {__-` \ \/ / \n"
                  "} '__}/  /\  \.-._} }  `-\ }\n"
                  "`----'`-'  `-'`----'     `-'\n"
                  "Tienes 20 intentos para descubrir la convinación.")
if dificultad == 2:
    print(magenta + "Has seleccionado la dificultad:\n"
                    ".-. .-. .---. .---. .-.  .-.  .--.  .-.   \n"
                    "|  \{ |/ {-. \} }}_}}  \/  { / {} \ } |   \n"
                    "| }\  {\ '-} /| } \ | {  } |/  /\  \} '--.\n"
                    "`-' `-' `---' `-'-' `-'  `-'`-'  `-'`----'\n"
                    "Tienes 12 intentos para descubrir la convinación.")
if dificultad == 3:
    print(red + "Has seleccionado la dificultad:\n"
                ".-. .-.  .--.  .---. .----.\n"
                "{ {_} | / {} \ } }}_}} {-. \ \n"
                "| { } }/  /\  \| } \ } '-} / \n"
                "`-' `-'`-'  `-'`-'-' `----' \n"
                "Tienes 6 intentos para descubrir la convinación.")

def jugador1():
    #Variable de tabla
    taula = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    #Inicializo fila
    fila = 0
    #While para rellenar la tabla
    while fila < 4:
        columna=0
        while columna < 4:
            #randint entre las 2 variables
            caracter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            taula[fila][columna]=caracter
            columna+=1
        fila+=1
    fila=0
    while fila < 1:
        print(magenta + f"{taula[fila]}")
        fila+=1

game = jugador1()