def imprimir_tra(b):
    for i in range(b):
        for j in range(b-i):
            print(" ", end="")
        for k in range(i+b):
            print(" *", end="")
        print()

b = int(input("Escribe el número de la base: "))  # Solicita al usuario el número de la base

imprimir_tra(b)
