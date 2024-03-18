
def suma (a,b) :
   "" "Aquesta funció retorna la suma dels paràmetres ai b"
   return a+b
print(f"************************************ ")
busca_valors = True
while busca_valors:   # Control d'errors
        try:      # Demana l'usuari que introdueixi el primer valor
            valor1= int(input("Primer valor a sumar "))
            busca_valors= False
        except ValueError:
            print(" Error, has d' introduir un valor enter, no pot introduir lletres ni caràcters especials" )   #Imprimir a la pantalla el misatge d'error

busca_valors = True
while busca_valors:   # Control d'errors
        try:      # Demana l'usuari que introdueixi el segon valor
            valor2= int(input("Segon valor a sumar "))
            busca_valors= False
        except ValueError:
            print(" Error, has d' introduir un valor enter, no pot introduir lletres ni caràcters especials" )   #Imprimir a la pantalla el misatge d'error

print(f"El resultat és: {suma(valor1,valor2)} ")
print(f"************************************ ")
