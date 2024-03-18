taula = [[0,0,0],
         [0,0,0],
         [0,0,0]]

print(f"************************************************")
print(f"Hauràs d'inserir valors en una taula de 3x3 " )
fila=0
while fila < 3:
    columna=0
    while columna < 3:
        caracter = (input("Insereix un caràcter "))
        taula[fila][columna]=caracter
        columna+=1
    fila+=1
print(f"************************************************")
print(f"Impressió d'un vector per files" )
fila=0
while fila < 3:
    print(taula[fila])
    fila+=1

