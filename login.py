import mysql.connector
from hashlib import sha256
from getpass import getpass
import os
import time
from datetime import datetime

db = None
cursor = None
sesion = None
opc_selected = None
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class bcolors:
    OK = '\033[92m' #VERDE
    WARNING = '\033[93m' #AMARILLO
    FAIL = '\033[91m' #ROJO
    RESET = '\033[0m' #REINICIAR COLOR

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def inicializar_database():
    try:
        global db, cursor
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_proyecto"
        )
        cursor = db.cursor()

        if db.is_connected():
            print("CONEXION EXITOSA")
            print("INICANDO...")
            time.sleep(1.5)
            limpiar_pantalla()
    except Exception as ex:
        print(ex)
        print("POR FAVOR CONTACTE CON UN ADMINISTRADOR")
        time.sleep(4)

def cerrar_conex_db():
    if cursor:
        cursor.close()
    if db:
        db.close()

def register():
    while True:
        while True:
            limpiar_pantalla()
            print("---------------------------------------")
            print("|               Registro              |")
            print("---------------------------------------")
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            password_verify = input("Vuelve a introducir la contraseña: ")

            if password == password_verify:
                print("Las contraseñas coinciden")
                time.sleep(1)
                break
            else:
                print("Las contraseñas no coinciden, vuelve a intentarlo")
                time.sleep(1)
                limpiar_pantalla()

        sql = "SELECT nombre_usuario FROM usuarios WHERE nombre_usuario = %s"  
        cursor.execute(sql, (username,))
        result = cursor.fetchone()

        if result is None:
            print("Registrando...")
            time.sleep(3)
            rol = 'user'
            ##Se cifra la contraseña
            salt = "s3cr3t5alt"
            hashed_password = sha256((password + salt).encode()).hexdigest()
            ##La conrtaseña se carga en la db
            sql = "INSERT INTO usuarios (nombre_usuario, contraseña, rol) VALUES (%s, %s, %s)"
            values = (username, hashed_password, rol)
            cursor.execute(sql, values)
            db.commit()
            #Se indica si el registro fue exitoso
            limpiar_pantalla()
            print("Usuario registrado correctamente.")
            time.sleep(1)
            # Registrar en el historial
            registrar_historial(f"Registro de usuario", username)
            break
        else:
            print("EL usuario ya existe, vuelve a intentarlo")
            time.sleep(1)

def login():
    global role, username, password
    limpiar_pantalla()
    print("---------------------------------------")
    print("|                Login                |")
    print("---------------------------------------")
    
    username = input("Nombre de usuario: ")
    password = getpass("Contraseña: ")

    sql = "SELECT contraseña, rol FROM usuarios WHERE nombre_usuario = %s"  
    cursor.execute(sql, (username,))
    result = cursor.fetchone()

    if result is None:
        print("Nombre de usuario incorrecto. Vuelve a intentarlo")
        time.sleep(1)
    else:
        hashed_password = result[0]
        role = result[1]
        salt = "s3cr3t5alt"
        entered_password = sha256((password + salt).encode()).hexdigest()
        if hashed_password == entered_password:
            limpiar_pantalla()
            if role == "admin":
                print("¡Bienvenido administrador!")
                menu_home()  # Se pasa el valor de 'role' a la función menu_home()
            else:
                print(f"Bienvenido @{username} inicio de sesión exitoso")
                menu_home()
            # Registrar en el historial
            registrar_historial(f"Inicio de sesión", username)
            return True
        else:
            print("Contraseña incorrecta.")
            time.sleep(1.5)
    return False

def change_password():
    limpiar_pantalla()
    print("---------------------------------------")
    print("|         Cambiar contraseña          |")
    print("---------------------------------------")
    username = input("Nombre de usuario: ")
    current_password = getpass("Contraseña actual: ")
    new_password = getpass("Nueva contraseña: ")

    sql = "SELECT contraseña FROM usuarios WHERE nombre_usuario = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()

    if result is None:
        print("Nombre de usuario incorrecto.")
    else:
        hashed_password = result[0]
        salt = "s3cr3t5alt"
        entered_password = sha256((current_password + salt).encode()).hexdigest()
        if hashed_password == entered_password:
            new_hashed_password = sha256((new_password + salt).encode()).hexdigest()
            update_sql = "UPDATE usuarios SET contraseña = %s WHERE nombre_usuario = %s"
            cursor.execute(update_sql, (new_hashed_password, username))
            db.commit()
            limpiar_pantalla()
            print("Contraseña actualizada correctamente.")
            # Registrar en el historial
            registrar_historial(f"Cambio de contraseña", username)
        else:
            limpiar_pantalla()
            print("Contraseña incorrecta.")

def opcion_incorrecta():
    print("Error: Opción Incorrecta")
    print("La opción seleccionada no es un número o no es una opción disponible")
    print("VUELVE A INTENTARLO")

def menu_principal():
    limpiar_pantalla()
    print("---------------------------------------")
    print("|            MENU PRINCIPAL           |")
    print("|-------------------------------------|")
    print("|  1.- Registro                       |")
    print("|  2.- Login                          |")
    print("|  3.- Cambiar contraseña             |")
    print("|  4.- Salir                          |")
    print("|-------------------------------------|")
    print("|Consult Date:", timestamp, "   |")
    print("---------------------------------------")

def seleccion():
    global opc_selected
    while True:
        try:
            opc_selected = int(input("Escribe la opción a seleccionar: "))
            return opc_selected
        except ValueError:
            opcion_incorrecta()
            time.sleep(0.5)
            limpiar_pantalla()

def mostrar_historial():
    sql = "SELECT * FROM historial WHERE usuario = %s ORDER BY fecha_hora DESC"  # Añadir %s para incluir el valor de 'username'
    cursor.execute(sql, (username,))
    result = cursor.fetchall()

    if result:
        limpiar_pantalla()
        print("--------------------------------------------")
        print("|                 Historial                |")
        print("--------------------------------------------")
        for row in result:
            print("ID de referencia:", row[0])
            print(bcolors.OK + "Acción:", row[1] + bcolors.RESET)
            print("Fecha y hora:", row[2])
            print("--------------------------------------------")

    else:
        print("No hay registros en el historial.")

def borrar_historial():
    limpiar_pantalla()
    confirmacion = input(bcolors.WARNING + "¿Estás seguro de que quieres borrar el historial? (s/n): " + bcolors.RESET)
    if confirmacion.lower() == 's':
        sql = "TRUNCATE TABLE historial"
        cursor.execute(sql)
        db.commit()
        time.sleep(1)
        print("Historial borrado correctamente.")
    else:
        print("Operación cancelada.")
        time.sleep(1)

def mostrar_usuarios():
    limpiar_pantalla()
    sql = "SELECT * FROM usuarios ORDER BY fecha_hora ASC"
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        print("------------------------------------------------")
        print("|            Uuarios registrados               |")
        print("------------------------------------------------")
        limpiar_pantalla()
        for row in result:
            print("ID de referencia:", row[0])
            print(bcolors.OK + "Acción:", row[1] + bcolors.RESET)
            print("Fecha y hora:", row[2])
            print(bcolors.OK + "Usuario:", row[3] + bcolors.RESET)
            print("---------------------------------------")
    else:
        print("No hay registros en el historial de usuarios.")



def eliminar_usuario():
    limpiar_pantalla()
    user = input(bcolors.WARNING + "Ingresa el nombre de usuario que deseas eliminar del sistema: " + bcolors.RESET)
    verify = getpass(bcolors.WARNING + "Ingresa tu contraseña administrador: " + bcolors.RESET)

    if verify == password:
        print(bcolors.OK + "\nLas contraseñas coinciden\n" + bcolors.RESET)
        time.sleep(0.5)
        confirmacion = input(bcolors.FAIL + "¿Estás seguro de que quieres eliminar al usuario? (s/n): " + bcolors.RESET)
        if confirmacion.lower() == 's':
            time.sleep(1)
            print(bcolors.WARNING + "Eliminando usuario..." + bcolors.RESET)
            sql = "DELETE FROM usuarios WHERE nombre_usuario = %s;"
            cursor.execute(sql, (user,))
            db.commit()
            time.sleep(2)
            print(bcolors.OK + "Usuario eliminado exitosamente" + bcolors.RESET)
            # Registrar en el historial
            registrar_historial(f"Eliminación de usuario", user)
        else: 
            print("Operación cancelada.")
            time.sleep(1)
    else:
        print("La contraseña no es correcta.")
        print("Cancelando operación...")
        time.sleep(1)

def mostrar_historial_admin():
    sql = "SELECT * FROM historial ORDER BY fecha_hora ASC"
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        limpiar_pantalla()
        print("---------------------------------------")
        print("|         Historial de Usuarios       |")
        print("---------------------------------------")
        for row in result:
            print("ID de referencia:", row[0])
            print(bcolors.OK + "Acción:", row[1] + bcolors.RESET)
            print("Fecha y hora:", row[2])
            print(bcolors.OK + "Usuario:", row[3] + bcolors.RESET)
            print("---------------------------------------")
    else:
        print("No hay registros en el historial de usuarios.")

def menu_admin():
    while True:
        print("---------------------------------------")
        print("|         MENÚ ADMINISTRADOR          |")
        print("|-------------------------------------|")
        print("| 1.- Mostrar Historial               |")
        print("| 2.- Borrar Historial                |")
        print("| 3.- Eliminar usuario                |")
        print("| 4.- Salir                           |")
        print("---------------------------------------")
        seleccion()

        if opc_selected == 1:
            mostrar_historial_admin()
            input("Presiona Enter para continuar...")
            limpiar_pantalla()
        elif opc_selected == 2:
            borrar_historial()
            input("Presiona Enter para continuar...")
            limpiar_pantalla()
        elif opc_selected == 3:
            eliminar_usuario()
            input("Presiona Enter para continuar...")
            limpiar_pantalla()
        elif opc_selected == 4:
            break
        else:
            opcion_incorrecta()

def menu_home():
    global sesion
    if sesion:
        while True:
            print("------------------------------")
            print("|     ¿Qué deseas hacer?     |")
            print("|----------------------------|")
            print("|   5.- Cambiar contraseña   |")
            if role == 'admin':
                print("|   6.- Menu Administrador   |")
            else:
                print("|   6.- Historial            |")
            print("|   7.- Salir                |")
            print("------------------------------")
            seleccion()

            if opc_selected == 5:
                change_password()
                input("Presiona Enter para continuar...")
                limpiar_pantalla()
            elif opc_selected == 6:
                if role == 'admin':
                    limpiar_pantalla()
                    menu_admin()
                    input("Presiona Enter para continuar...")
                    limpiar_pantalla()
                else:
                    limpiar_pantalla()
                    mostrar_historial()
                    input("Presiona Enter para continuar...")
                    limpiar_pantalla()
            elif opc_selected == 7:
                sesion = False
                break
            else:
                opcion_incorrecta()

def registrar_historial(accion, username):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO historial (accion, fecha_hora, usuario) VALUES (%s, %s, %s)"
    values = (accion, timestamp, username)
    cursor.execute(sql, values)
    db.commit()

try:
    inicializar_database()

    while True:
        menu_principal()
        seleccion()

        if opc_selected == 1:
            register()
            input("Presiona Enter para continuar...")
            limpiar_pantalla()
        elif opc_selected == 2:
            sesion = login()
            if sesion:
                while sesion:
                    menu_home()
                    limpiar_pantalla()
        elif opc_selected == 3:
            change_password()
            input("Presiona Enter para continuar...")
            limpiar_pantalla()
        elif opc_selected == 4:
            limpiar_pantalla()
            print("SALIENDO...")
            time.sleep(1)
            limpiar_pantalla()
            break
        else:
            opcion_incorrecta()

except Exception as ex:
    print(ex)

finally:
    cerrar_conex_db()

