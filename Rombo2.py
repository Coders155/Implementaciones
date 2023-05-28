def imprimir_Rombo(lado):
    for i in range(lado):
        for j in range(lado-i):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        print()
    for i in range(lado-1):
        for j in range(i+2):
            print(" ", end="")
        for j in range(2*(lado-i-2)+1):
            print("*", end="")
        print()

lado = int(input("Escribe la medida del rombo: "))  # Solicita al usuario la medida del rombo

print("Rombo:")
imprimir_Rombo(lado)
