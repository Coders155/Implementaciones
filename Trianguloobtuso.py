def imprimir_tri(ba):
    for i in range(ba + 1):
        for j in range(i + ba):
            print(" ", end=" ")  # Imprime espacios en blanco
        for k in range(i):
            print(" ", end="*")  # Imprime asteriscos
        print()  # Imprime una nueva línea

ba = int(input("Escribe la medida de la base: "))  # Solicita al usuario la medida de la base

imprimir_tri(ba)
