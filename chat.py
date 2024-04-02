import random


def generar_combinacion():
    """Genera una combinación aleatoria de letras."""
    letras_posibles = ['A', 'B', 'C', 'D', 'E', 'F']
    combinacion = []
    for _ in range(4):
        letra = random.choice(letras_posibles)
        combinacion.append(letra)
    return combinacion


def obtener_intentos():
    """Solicita al jugador una combinación de letras."""
    while True:
        intento = input("Intenta adivinar la combinación (4 letras de A a F sin espacios): ").upper()
        if len(intento) != 4 or not all(letra in 'ABCDEF' for letra in intento):
            print("Por favor, ingresa una combinación válida de 4 letras de A a F.")
        else:
            return list(intento)


def verificar_combinacion(combinacion_secreta, intento):
    """Verifica si el intento del jugador coincide con la combinación secreta."""
    colocacion_correcta = 0
    color_correcto = 0
    for i in range(4):
        if intento[i] == combinacion_secreta[i]:
            colocacion_correcta += 1
        elif intento[i] in combinacion_secreta:
            color_correcto += 1
    return colocacion_correcta, color_correcto


def imprimir_resultado(colocacion_correcta, color_correcto):
    """Imprime el resultado del intento."""
    resultado = 'X' * colocacion_correcta + '.' * color_correcto
    print(f"Resultado: {resultado}")


def jugar_mastermind():
    """Función principal para ejecutar el juego."""
    print("¡Bienvenido a Mastermind!\n")
    combinacion_secreta = generar_combinacion()

    for intento_actual in range(1, 11):
        print(f"Intento #{intento_actual}")
        intento = obtener_intentos()

        colocacion_correcta, color_correcto = verificar_combinacion(combinacion_secreta, intento)
        imprimir_resultado(colocacion_correcta, color_correcto)

        if colocacion_correcta == 4:
            print("¡Felicidades! Has adivinado la combinación secreta.")
            return

    print("¡Se te acabaron los intentos! La combinación secreta era:", ''.join(combinacion_secreta))


# Ejecutar el juego
jugar_mastermind()
