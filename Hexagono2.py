lado = int(input("Lado: "))  # Solicita al usuario el tamaño del lado del triángulo
espacios = lado - 1  # Inicializa la variable 'espacios' con el valor del lado menos 1

# Bucle para imprimir las líneas superiores del triángulo
for i in range(lado, 3 * lado, 2):
    print("  " * espacios + " *" * i)  # Imprime los espacios seguidos de los asteriscos
    espacios -= 1  # Reduce el número de espacios en cada iteración

espacios = 1  # Restablece el valor de 'espacios' a 1

# Bucle para imprimir las líneas inferiores del triángulo
for i in range(3 * lado - 4, lado - 2, -2):
    print("  " * espacios + " *" * i)  # Imprime los espacios seguidos de los asteriscos
    espacios += 1  # Aumenta el número de espacios en cada iteración
