import  random

#Colores
green = "\033[0;92m"
magenta = "\033[0;95m"
red = "\033[0;91m"

def conterror():
    control = True
    while control == True:
        try:
            val = int(input(green + "Introduce un valor: "))
            control = False
            return val
        except ValueError:
            print(red + "El valor ha de ser un numero entero")

print(green + f"Valor minimo")
min = conterror()
print(green + f"Valor maximo")
max = conterror()

taula = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

fila=0

while fila < 4:
    columna=0
    while columna < 4:
        caracter = random.randint(min, max)
        taula[fila][columna]=caracter
        columna+=1
    fila+=1

fila=0
print(magenta + f"\nTabla:")
while fila < 4:
    print(f"{taula[fila]}")
    fila+=1
