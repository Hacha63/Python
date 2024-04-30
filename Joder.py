#Importamos la libreria random
import  random
import os



#Colores
green = "\033[0;92m"
magenta = "\033[0;95m"
red = "\033[0;91m"

#Introduccion
print(magenta + "    __  ___           __                      _           __\n"
                "   /  |/  /___ ______/ /____  _________ ___  (_)___  ____/ /\n"
                r"  / /|_/ / __ `/ ___/ __/ _ \/ ___/ __ `__ \/ / __ \/ __  /""\n"
                " / /  / / /_/ (__  ) /_/  __/ /  / / / / / / / / / / /_/ /\n"
                r"/_/  /_/\__,_/____/\__/\___/_/  /_/ /_/ /_/_/_/ /_/\__,_/""\n")
print(magenta + "@ Significa que hay un numero correcto en una posición correcta.\n"
                "& Significa que hay un numero correcto pero en una posición erronea.")
#Def con control de errores para elejir si hay 1 o 2 jugadores.
def jugadores():
    control = True
    print(magenta +  "    o     |    o   o \n"
                    r"   /|\    |   /|\ /|\ ""\n"
                    r"   / \    |   / \ / \ ""\n"
                    r"    1     |      2   ""\n")

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

#Def para elejir la dificultad con control de errores
def dif():
    control = True
    print(green +  ".----.  .--.   .----..-.  .-.    .-. .-. .---. .---. .-.  .-.  .--.  .-.       .-. .-.  .--.  .---. .----.\n"
                  r"} |__} / {} \ { {__-` \ \/ /     |  \{ |/ {-. \} }}_}}  \/  { / {} \ } |       { {_} | / {} \ } }}_}} {-. \ ""\n"
                  r"} '__}/  /\  \.-._} } `-\ }     | }\  {\ '-} /| } \ | {  } |/  /\  \} '--.    | { } }/  /\  \| } \ } '-} / ""\n"
                   "`----'`-'  `-'`----'    `-'     `-' `-' `---' `-'-' `-'  `-'`-'  `-'`----'    `-' `-'`-'  `-'`-'-' `----' \n"
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

#Def para generar la combinacion secreta. Elije entre las letras de la tabla
def generar_combinacion():
    letras_posibles = ["A", "B", "C", "D", "E", "F"]
    combinacion = []
    for _ in range(4):
        letra = random.choice(letras_posibles)
        combinacion.append(letra)

    return combinacion
#Def para mostrar el tablero
def mostrar(taula,fila,difi):
    fila=0
    #Colores
    green = "\033[0;92m"
    magenta = "\033[0;95m"
    print(green + f"Intenta adivinar la combinación de las letras A, B, C, D, E, F: Ejemplo: ABCD")
    #Mostrar tabla entendible
    while fila < difi:
        print(magenta + f"{taula[fila]}")
        fila+=1
def jugar_mastermind(difi):
    #Tabla donde guardaremos las jugadas
    taula = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    fila = 0
    quedan = difi
    print(magenta + "¡Bienvenido a Mastermind!\n")
    #Llama el def para elejir los jugadores y compara el resultado, si la eleccion no es 1, (2) nos lleva a otro def donde la combinación se elije
    if jugadores() == 1:
        combinacion_secreta = generar_combinacion()
        #Ver combinacion aleatoria
        dev = input("Dev Mode? (YES or NO): ").upper()
        if dev == "YES":
            print (combinacion_secreta)
    else:
        combinacion_secreta = jugador2()

    #Explicacion del juego
    print(green + f"Intenta adivinar la combinación de las letras A, B, C, D, E, F: Ejemplo: ABCD")
    #Los intentos tienen el rango entre 1 y la dificultad ya sean 7, 12 o 20 intentos.
    for intento_actual in range(1, difi):
        while fila < difi:
            columna = 0
            while columna < 4:
                intento = obtener_intentos()
                colocacion_correcta, letra_correcta = verificar_combinacion(combinacion_secreta,intento)
                resultado = "@" * colocacion_correcta + "&" * letra_correcta
                taula[fila][columna] = intento
                columna += 1
                taula[fila][columna] = intento_actual
                columna += 1
                taula[fila][columna] = resultado
                columna += 1
                quedan = quedan - 1
                taula[fila][columna] = quedan
                #Mostrar tablero
                mostrar(taula, fila, difi)
                columna += 1
                if colocacion_correcta == 4:
                    print(green + " __      __  _____    _____   _______    ____    _____    _____            \n"
                                  r" \ \    / / |_   _|  / ____| |__   __|  / __ \  |  __ \  |_   _|     /\    ""\n"
                                  r"  \ \  / /    | |   | |         | |    | |  | | | |__) |   | |      /  \   ""\n"
                                  r"   \ \/ /     | |   | |         | |    | |  | | |  _  /    | |     / /\ \  ""\n"
                                  r"    \  /     _| |_  | |____     | |    | |__| | | | \ \   _| |_   / ____ \ ""\n"
                                  r"     \/     |_____|  \_____|    |_|     \____/  |_|  \_\ |_____| /_/    \_\  ")
                    return
            fila += 1



        #Si la variable colocacion_correcta tiene las 4 letras correctas ganas

    print(red + "  _____    ______   _____    _____     ____    _______            \n"
                r" |  __ \  |  ____| |  __ \  |  __ \   / __ \  |__   __|     /\    ""\n"
                r" | |  | | | |__    | |__) | | |__) | | |  | |    | |       /  \   ""\n"
                r" | |  | | |  __|   |  _  /  |  _  /  | |  | |    | |      / /\ \  ""\n"
                r" | |__| | | |____  | | \ \  | | \ \  | |__| |    | |     / ____ \ ""\n"
                r" |_____/  |______| |_|  \_\ |_|  \_\  \____/     |_|    /_/    \_\ ")
    print(red + f"La combinachión era {combinacion_secreta}")

#Def para imprimir resulados si son correctos o no usa & o @

#Compara la combinacion del intento que hemos introducido con la combinación que ha generado de la tabla en el def anterior
def verificar_combinacion(combinacion_secreta, intento):
    colocacion_correcta = 0
    letra_correcta = 0
    #Depenjdiendo si és correcto se suman las variables y el def imprimir resultados muestra
    for i in range(4):
        if intento[i] == combinacion_secreta[i]:
            colocacion_correcta += 1
        elif intento[i] in combinacion_secreta:
            letra_correcta += 1
    return colocacion_correcta, letra_correcta
#Este def es para introducir los intentos para adivinadlo. Tiene control de errores y aunque lo introduzcas en minuscula la funcion .upper() las traduce automaticamente.
def obtener_intentos():
    while True:
        intento = input().upper()
        #Control de errores
        if len(intento) != 4 or not all(letra in 'ABCDEF' for letra in intento):
            print(red + "Por favor, ingresa una combinación válida de 4 letras de A a F.")
        else:
            #Devolvemos el input como lista para compararlo después
            return list(intento)
#Este def es para cuando se selecciona 2 jugadores. La combinacion secreta no se genera. Se introduce por el segundo jugador.
#Esto hay que mejorarlo porque el input es visible
def jugador2():
    blanco = 0
    print(magenta + "Introduce la combinación secreta de 4 letras de la A a F: Ejemplo: ABCD")
    #Control de errores
    while True:
        combinacion = input().upper()
        if len(combinacion) != 4 or not all(letra in 'ABCDEF' for letra in combinacion):
            print(red + "Por favor, ingresa una combinación válida de 4 letras de A a F.")
        else:
            while blanco != 20:
                print(" \n")
                blanco = blanco + 1
            return list(combinacion)


#Llama al def para seleccionar la dificultad
dificultad = dif()

#If que comparan si la dificultad es 1, 2 o 3 para definir los intentos maximos en difi
#Tambien muestra que dificultad has introducido
if dificultad == 1:
    print(green + "Has seleccionado la dificutlad:\n"
                  r".----.  .--.   .----. .-.  .-. ""\n"
                  r"} |__} / {} \ { {__-`  \ \/ / ""\n"
                  r"} '__}/  /\  \.-._} } `-\ } ""\n"
                  r"`----'`-'  `-'`----'    `-' ""\n"
                  "Tienes 20 intentos para descubrir la convinación.")
    difi = 20
if dificultad == 2:
    print(magenta + "Has seleccionado la dificultad:\n"
                    r".-. .-. .---. .---. .-.  .-.  .--.  .-.   ""\n"
                    r"|  \{ |/ {-. \} }}_}}  \/  { / {} \ } |   ""\n"
                    r"| }\  {\ '-} /| } \ | {  } |/  /\  \} '--. ""\n"
                    r"`-' `-' `---' `-'-' `-'  `-'`-'  `-'`----' ""\n"
                    "Tienes 12 intentos para descubrir la convinación.")
    difi = 12
if dificultad == 3:
    print(red + "Has seleccionado la dificultad:\n"
                r".-. .-.  .--.  .---. .----. ""\n"
                r"{ {_} | / {} \ } }}_}} {-. \ ""\n"
                r"| { } }/  /\  \| } \ } '-} / ""\n"
                r"`-' `-'`-'  `-'`-'-' `----' ""\n"
                "Tienes 7 intentos para descubrir la convinación.")
    difi = 7

#Llamamos al def principal para empezar a jugar y a la variable difi le asignamos difi para el numero de intentos segun la dificultad
difi = jugar_mastermind(difi)
