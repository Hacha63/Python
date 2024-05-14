#Importamos la libreria random
import  random
import subprocess



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
def mostrar(taula,fila,difi,tab_max):
    fila=0
    #Colores
    green = "\033[0;92m"
    magenta = "\033[0;95m"
    print(green + f"Intenta adivinar la combinación de las letras A, B, C, D, E, F: Ejemplo: ABCD")
    #Mostrar tabla entendible
    while fila < tab_max:
        print(magenta + f"{taula[fila]}")
        fila+=1
#Def principal para la iniciación del juego
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

    else:
        combinacion_secreta = jugador2()

    #Explicacion del juego
    print(green + f"Intenta adivinar la combinación de las letras A, B, C, D, E, F: Ejemplo: ABCD")
    #Los intentos tienen el rango entre 1 y la dificultad ya sean 7, 12 o 20 intentos.
    for intento_actual in range(1, difi):
    #2 While para ir rellenando las filas y columnas con los datos necesarios
        while fila < difi:
            columna = 0
            while columna < 4:
                blanco = 0
                intento = obtener_intentos()
                #Multiplica la variable colocacion corrcta y letra correcta para ver cuantos @ y & hay
                colocacion_correcta, letra_correcta, trampa = verificar_combinacion(combinacion_secreta,intento)
                resultado = "@" * colocacion_correcta + "&" * letra_correcta
                #Rellena el numero de intento
                taula[fila][columna] = f"Intento nº: {intento_actual}"
                #Esta variable tab_max es para que la tabla se muestre hasta el limite de intento
                tab_max = intento_actual
                intento_actual = intento_actual + 1
                columna += 1
                #Mostrar input
                taula[fila][columna] = intento
                columna += 1
                #Mostrar resultado
                taula[fila][columna] = resultado
                columna += 1
                quedan = quedan - 1
                #Mostrar jugadas restantes
                taula[fila][columna] = f"Jugadas restantes: {quedan}"
                #Espacio entre tabla
                while blanco != 20:
                    print(" \n")
                    blanco = blanco + 1
                #Mostrar tablero
                mostrar(taula, fila, difi, tab_max)
                #Mostrar codigo secreto si se introduce ###
                if trampa > 0:
                    print(combinacion_secreta)
                columna += 1

                #Ascii de victoria si las 4 letras son correctas
                if colocacion_correcta == 4:
                    print(green + "**********************************************************************************""\n"
                                   "*   __      __  _____    _____   _______    ____    _____    _____              *\n"
                                  r"*   \ \    / / |_   _|  / ____| |__   __|  / __ \  |  __ \  |_   _|     /\      *""\n"
                                  r"*    \ \  / /    | |   | |         | |    | |  | | | |__) |   | |      /  \     *""\n"
                                  r"*     \ \/ /     | |   | |         | |    | |  | | |  _  /    | |     / /\ \    *""\n"
                                  r"*      \  /     _| |_  | |____     | |    | |__| | | | \ \   _| |_   / ____ \   *""\n"
                                  r"*       \/     |_____|  \_____|    |_|     \____/  |_|  \_\ |_____| /_/    \_\  *""\n"
                                  f"*  La combinachión era {combinacion_secreta}                                     *""\n"
                                   "*********************************************************************************")
                    return
            fila += 1



        #Si se te acaban los intentos pierdes

    print(red +  "************************************************************************""\n"
                 "*    _____    ______   _____    _____     ____    _______              *""\n"
                r"*   |  __ \  |  ____| |  __ \  |  __ \   / __ \  |__   __|     /\      *""\n"
                r"*   | |  | | | |__    | |__) | | |__) | | |  | |    | |       /  \     *""\n"
                r"*   | |  | | |  __|   |  _  /  |  _  /  | |  | |    | |      / /\ \    *""\n"
                r"*   | |__| | | |____  | | \ \  | | \ \  | |__| |    | |     / ____ \   *""\n"
                r"*   |_____/  |______| |_|  \_\ |_|  \_\  \____/     |_|    /_/    \_\  *""\n"
                f"*  La combinachión era {combinacion_secreta}                            *""\n"
                 "************************************************************************")
    #Rick Roll, el baile de perder
    subprocess.Popen(["start", "cmd", "/c", "curl.exe -sN http://rick.jachan.dev"], shell=True)



#Compara la combinacion del intento que hemos introducido con la combinación que ha generado de la tabla en el def anterior
#He modificado este def para justar mejor los resultados @ y &.
def verificar_combinacion(combinacion_secreta, intento):
    colocacion_correcta = 0
    letra_correcta = 0
    #variable para las trampas
    trampa = 0
    #Hago una copia del la combinacion secreta y del intento
    combinacion_secreta_copy = combinacion_secreta.copy()
    intento_copia = intento.copy()
    #Si en el input hay # se suma la variable trampa y se mostrará el codigo secreto
    for i in range(4):
        if intento_copia[i] == "#":
            trampa = trampa + 1
    #Primero verificamos las letras bien puestas
    for i in range(4):
        if intento_copia[i] == combinacion_secreta[i]:
            colocacion_correcta += 1
            #Marco la posicion de [i] de la combinacion como None, para que no me la lea otra vez en el siguiente for
            #Cambio la posicion [i] de la copia del intento y la aplaso por una X para que no me la encuentre otra vez por error
            combinacion_secreta_copy[i] = None
            intento_copia[i] = "X"
    #Luego verificamos las letras correctas pero en posiciones incorrectas
    for letra in intento_copia:
        if letra in combinacion_secreta_copy and letra != None:
            letra_correcta += 1
            #Marcamos la letra como encontrada para no contarla dos veces
            combinacion_secreta_copy.remove(letra)

    return colocacion_correcta, letra_correcta, trampa


#Este def es para introducir los intentos para adivinadlo. Tiene control de errores y aunque lo introduzcas en minuscula la funcion .upper() las traduce automaticamente.
def obtener_intentos():
    while True:
        intento = input().upper()
        #Control de errores, en el listado de caracteres permitidos he añadido # para que se puedan hacer trampas
        if len(intento) != 4 or not all(letra in 'ABCDEF#' for letra in intento):
            print(red + "Por favor, ingresa una combinación válida de 4 letras de A a F.")
        else:
            #Devolvemos el input como lista para compararlo después
            return list(intento)
#Este def es para cuando se selecciona 2 jugadores. La combinacion secreta no se genera. Se introduce por el segundo jugador.
def jugador2():
    blanco = 0
    print(magenta + "Introduce la combinación secreta de 4 letras de la A a F: Ejemplo: ABCD")
    #Control de errores
    while True:
        combinacion = input().upper()
        if len(combinacion) != 4 or not all(letra in 'ABCDEF' for letra in combinacion):
            print(red + "Por favor, ingresa una combinación válida de 4 letras de A a F.")
        else:
            #Espacio para no ver el codigo del compañero
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
jugar_mastermind(difi)
