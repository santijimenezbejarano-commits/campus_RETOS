numero_secreto = 42
intentos = 0
adivinado = False

print("¡Bienvenido al juego de Adivina el Número!")
print("Estoy pensando en un número... ¿Podrás adivinar cuál es?")
print("---------------------------------------------------")

while not adivinado:

    intento_usuario = int(input("Introduce tu número: "))
    intentos += 1 

    if intento_usuario == numero_secreto:

        adivinado = True
        print(f"\n¡Felicidades! 🎉 Has adivinado el número secreto ({numero_secreto}).")
        print(f"Te tomó un total de {intentos} intentos.")
    
    elif intento_usuario < numero_secreto:
        print("Demasiado bajo. 👇 ¡Inténtalo de nuevo!")
    
    else:
        print("Demasiado alto. 👆 ¡Inténtalo de nuevo!")