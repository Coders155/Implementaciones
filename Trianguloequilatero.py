A = int(input("Escribe la medida: "))  # Solicita al usuario la medida

for i in range(A):
    espacios = A - i  # Calcula el número de espacios en cada línea
    print(" " * espacios + "* " * i)  # Imprime los espacios seguidos de los asteriscos
