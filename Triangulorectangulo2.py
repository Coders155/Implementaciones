def imprimir_triangulorectangulo(lado):
    for i in range(lado):
        for j in range(lado - i):
            print("", end="")  # Imprime espacios en blanco
        for j in range(2 * i + 1):
            print("*", end=" ")  # Imprime asteriscos seguidos de un espacio
        print()  # Imprime una nueva línea

lado = int(input("Ingrese la medida del lado de la figura, un entero positivo: "))  # Solicita al usuario la medida del lado

print("Triángulo rectángulo:")

imprimir_triangulorectangulo(lado)
