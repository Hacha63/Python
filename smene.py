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
                print(red + "Elije entre 1 o 2 jugadores.")
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

#AAAA
def generar_combinacion():
    letras_posibles = ['A', 'B', 'C', 'D', 'E', 'F']
    combinacion = []
    for _ in range(4):
        letra = random.choice(letras_posibles)
        combinacion.append(letra)
    print(f"{combinacion}")
    return combinacion
def jugar_mastermind(difi):
    intcorrecto = False
    print("¡Bienvenido a Mastermind!\n")
    if jugadores() == 1:
        combinacion_secreta = generar_combinacion()
    else:
        combinacion_secreta = input("Introduce la combinación entre A y F: ")

    for intento_actual in range(1, difi):
        print(f"Intento {intento_actual}")
        intento = obtener_intentos()
        colocacion_correcta, color_correcto = verificar_combinacion(combinacion_secreta, intento)
        imprimir_resultado(colocacion_correcta, color_correcto)

        if colocacion_correcta == 4:
            print("Combinación correcta")
            return
        print("¡Se te acabaron los intentos! La combinación secreta era:", ''.join(combinacion_secreta))

def imprimir_resultado(colocacion_correcta, color_correcto):
    resultado = 'X' * colocacion_correcta + '.' * color_correcto
    print(f"Resultado: {resultado}")

def verificar_combinacion(combinacion_secreta, intento):
    colocacion_correcta = 0
    color_correcto = 0
    for i in range(4):
        if intento[i] == combinacion_secreta[i]:
            colocacion_correcta += 1
        elif intento[i] in combinacion_secreta:
            color_correcto += 1
    return colocacion_correcta, color_correcto

def obtener_intentos():
    print(f"Intenta adivinar la combinación de las letras A, B, C, D, E, F: ")
    while True:
        intento = input().upper()
        if len(intento) != 4 or not all(letra in 'ABCDEF' for letra in intento):
            print("Por favor, ingresa una combinación válida de 4 letras de A a F.")
        else:
            return list(intento)
#AAA


dificultad = dif()


if dificultad == 1:
    print(green + "Has seleccionado la dificutlad:\n"
                  ".----.  .--.   .----..-.  .-.\n"
                  "} |__} / {} \ { {__-` \ \/ / \n"
                  "} '__}/  /\  \.-._} }  `-\ }\n"
                  "`----'`-'  `-'`----'     `-'\n"
                  "Tienes 20 intentos para descubrir la convinación.")
    difi = 20
if dificultad == 2:
    print(magenta + "Has seleccionado la dificultad:\n"
                    ".-. .-. .---. .---. .-.  .-.  .--.  .-.   \n"
                    "|  \{ |/ {-. \} }}_}}  \/  { / {} \ } |   \n"
                    "| }\  {\ '-} /| } \ | {  } |/  /\  \} '--.\n"
                    "`-' `-' `---' `-'-' `-'  `-'`-'  `-'`----'\n"
                    "Tienes 12 intentos para descubrir la convinación.")
    difi = 12
if dificultad == 3:
    print(red + "Has seleccionado la dificultad:\n"
                ".-. .-.  .--.  .---. .----.\n"
                "{ {_} | / {} \ } }}_}} {-. \ \n"
                "| { } }/  /\  \| } \ } '-} / \n"
                "`-' `-'`-'  `-'`-'-' `----' \n"
                "Tienes 10 intentos para descubrir la convinación.")
    difi = 10


difi = jugar_mastermind(difi)
