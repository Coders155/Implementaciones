"""                LIBRERIAS                     """
import os
import matplotlib.pyplot as plt
import time
import numpy as np
from matplotlib.patches import Ellipse
## DEFINICION DE METODOS##
# Metodos de uso general


def seleccion():
    global opc_selected
    global opc_especial

    while True:
        try:
            opc_selected = int(input("Escribe la opción a seleccionar: "))
            opc_especial = opc_selected
            return opc_selected, opc_especial
        except ValueError:
            opcion_incorrecta()
            time.sleep(0.5)
            limpiar_pantalla()
            menu_principal()


def opcion_incorrecta():
    print("Error: Opción Incorrecta")
    print("La opción seleccionada no es un número o no es una opción disponible")
    print("VUELVE A INTENTARLO")


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Metodo para interfaz


def menu_principal():

    global opc_selected
    global opc_especial

    while True:
        limpiar_pantalla()
        print("""
                Menú Principal
    -------------------------------------
    |¿Que figura necesitas?             |
    -------------------------------------
    | 1-Triángulos                      |
    | 2-Cuadrilateros                   |
    | 3-Pentagonos                      |
    | 4-Hexagonos                       |
    | 5-Circulos (Ovalos)               |
    -------------------------------------
    """)

        seleccion()

        if opc_selected == 1:
            sub_menu_triangulos()
        elif opc_selected == 2:
            # sub_menu_cuadrilateros()
            print("Menu en construccion")
        elif opc_selected == 3:
            # sub_menu_pentagonos()
            print("Menu en construccion")
        elif opc_selected == 4:
            # sub_menu_hexagonos()
            print("Menu en construccion")
        elif opc_selected == 5:
            # sub_menu_elipses()
            print("Menu en construccion")
        elif opc_selected == 155:
            admin()
        else:
            opcion_incorrecta()

# Metodo para interfaz


def admin():
    limpiar_pantalla()
    print("Entrando al menu admin")


def sub_menu_triangulos():
    global opc_selected

    while True:
        time.sleep(0.5)
        limpiar_pantalla()
        print("""
                Sub-Menú
        -------------------------
        |  Tipos de triangulos  |
        -------------------------
        |      1-Equilatero     |
        |      2-Escaleno       |
        |      3-Isosceles      |
        -------------------------
        """)

        seleccion()
        if opc_selected == 1:
            generar_TriEquilatero()
        elif opc_selected == 2:
            generar_TriEscaleno()
        elif opc_selected == 3:
            generar_TriIsoceles()
        else:
            print("Opción Invalida. Vuelve a intentarlo")


def generar_TriEquilatero():
    limpiar_pantalla()
    print("TRIANGULO EQUILATERO")
    a = int(input("Introduce el valor para todos los lados: "))
    fig, ax = plt.subplots()
    plt.title("TRIANGULO EQUILATERO")
    # El primero es para Este y Oeste
    # El segundo es para Norte y Sur
    ax.plot([0, a], [0, 0])  # Base
    ax.plot([0, (a/2)], [0, a])  # Lado A
    ax.plot([(a/2), a], [a, 0])  # Lado B
    ax.plot([(a/2), (a/2)], [0, a])  # Altura
    plt.show()


def generar_TriEscaleno():
    limpiar_pantalla()
    print("TRIANGULO ESCALENO")
    ba = int(input("Inserte cm de Base: "))
    a = int(input("Inserte cm de Lado A: "))
    fig, ax = plt.subplots()
    plt.title("TRIANGULO EQUILATERO")
    # El primero es para Este y Oeste
    # El segundo es para Norte y Sur
    ax.plot([0, ba], [0, 0])  # Base
    ax.plot([0, ba], [0, a])  # Lado A
    ax.plot([ba, ba], [a, 0])  # Lado B
    ax.plot([ba, ba/2], [a, 0])
    plt.show()


def generar_TriIsoceles():
    limpiar_pantalla()
    print("TRIANGULO ISOSELES")
    a = int(input("Introduce el valor de la base (en cm): "))
    l = int(input("Introduce los valores de los lados (en cm): "))
    fig, ax = plt.subplots()
    plt.title("TRIANGULO ISOSCELES")
    # El primero es para Este y Oeste
    # El segundo es para Norte y Sur
    ax.plot([0, a], [0, 0])  # Base
    ax.plot([0, (a/2)], [0, l])  # Lado A
    ax.plot([(a/2), a], [l, 0])  # Lado B
    ax.plot([(a/2), (a/2)], [0, l])  # Altura
    plt.show()

# Metodo para interfaz


def sub_menu_elipses():
    limpiar_pantalla()
    print("""

    ----------------------------
    |          Menú            |
    ----------------------------
    |Tipos de Circulo u Ovalos |
    ----------------------------
    |        1-Circulo         |
    |        2-Ovoide          |
    |        3-Ovalo           |
    ----------------------------

    """)

    seleccion()

    if opc_selected == 1:
        generar_Circulo()
    elif opc_selected == 2:
        generar_Ovalo()
    elif opc_selected == 3:
        generar_Ovoide()
    else:
        opcion_incorrecta()


def generar_Circulo():
    print("CIRCULO")
    r = int(input("Introduzca el tamañano del radio que desea: "))
    fig, ax = plt.subplots()
    plt.title("CIRCULO")
    circle = plt.Circle((r, r), radius=r,)
    ax.add_patch(circle)
    ax.set_xlim((0, r*2))
    ax.set_ylim((0, r*2))
    plt.show()


def generar_Ovalo():
    print("OVALO")
    r = int(input("Introduce el radio del Ovalo: "))
    fig, ax = plt.subplots()
    plt.title("OVALO")
    ellipse = Ellipse((r, r/2), width=r*2, height=r, )
    ax.add_patch(ellipse)
    ax.set_xlim((0, r*2))
    ax.set_ylim((0, r*2))
    plt.show()


def generar_Ovoide():
    print("OVOIDE")
    r = int(input("Introduce el radio del Ovoide: "))
    fig, ax = plt.subplots()
    plt.title("OVOIDE")
    Ovoide = Ellipse((r, r), width=r, height=r*2, )
    ax.add_patch(Ovoide)
    ax.set_xlim((0, r*3))
    ax.set_ylim((0, r*3))
    plt.show()


menu_principal()
