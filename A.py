import  random
taula = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
def mostrar(taula,fila):
    fila=0
    while fila < 3:
        print(taula[fila])
        fila+=1
jugada = 1
intento = 0
resultado = "%%%%"
print(f"************************************************")
print(f"Hauràs d'inserir valors en una taula de 3x3 " )
fila=0
def inputt():
    intento = input("Input: ")
    return  intento

while fila < 3:
    columna=0
    while columna < 3:
        resultado = random.random()
        intento = inputt()
        taula[fila][columna]=intento
        columna+=1
        taula[fila][columna] = jugada
        columna+=1
        taula[fila][columna] = resultado
        mostrar(taula,fila)
        columna+=1
        jugada+=1
    fila+=1
