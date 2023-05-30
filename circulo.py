import math

def dibujar_circulo(radio):
    for y in range(-radio, radio + 1):
        for x in range(-radio, radio + 1):
            distancia = math.sqrt(x**2 + y**2)
            if distancia <= radio + 0.5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Solicitar al usuario el radio del círculo
radio = int(input("Ingresa el radio del círculo: "))

# Llamar a la función para dibujar el círculo
dibujar_circulo(radio)
