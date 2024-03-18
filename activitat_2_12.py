#Importamos la libreria random
import  random

#Colores
green = "\033[0;92m"
magenta = "\033[0;95m"
red = "\033[0;91m"

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
#Explicación
print(magenta + f"Introduce el primer numero para definir el valor minimo y despues introduce el maximo.\nLa tabla se rellenara con un intervalo entre esos numeros")

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