#Colores
green = "\033[0;92m"
magenta = "\033[0;95m"
red = "\033[0;91m"

#def introducir numeros y control de errores entre 0 y 100
def conterror():
    control = True
    while control == True:
        try:
            val = int(input(green + "Introduce uno a uno los numeros: "))
            if (0 <= val <= 100):
                control = False
                return val
            else:
               print(red + "El valor ha de ser un numero entre 0 y 100")
        except ValueError:
            print(red + "El valor ha de ser un numero entero")
#def para comparar numeros y devolver en orden
def minmitmax(a, b, c):
    if a <= b <= c:
        return a, b, c
    elif a <= c <= b:
        return a, c, b
    elif b <= a <= c:
        return b, a, c
    elif b <= c <= a:
        return b, c, a
    elif c <= a <= b:
        return c, a, b
    else:
        return c, b, a

#Asignar 3 valores a 3 variables repitiendo 3 veces el def conterror
val1 = conterror()
val2= conterror()
val3= conterror()

#Asignar variables min, mit y max del def minmitmax
min, mit, max = minmitmax(val3, val2, val1)

#Mostrar resultados
print(magenta + f"El valor minimo és: {min}\nEl valor medio és: {mit}\nEl valor máximo és: {max}")