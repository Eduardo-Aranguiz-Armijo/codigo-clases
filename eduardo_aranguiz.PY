usuarios = {}

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if " " in contraseña:
        return False
    tiene_letra = any(c.isalpha() for c in contraseña)
    tiene_numero = any(c.isdigit() for c in contraseña)
    return tiene_letra and tiene_numero

def ingresar_usuario():
    while True:
        nombre = input("Ingrese nombre de usuario: ")
        if nombre in usuarios:
            print("Usuario ya existe. Intente otro.")
        else:
            break

    while True:
        sexo = input("Ingrese sexo (M/F): ").upper()
        if sexo in ["M", "F"]:
            break
        else:
            print("Debe ingresar M o F solamente. Intente de nuevo.")

    while True:
        contraseña = input("Ingrese contraseña: ")
        if validar_contraseña(contraseña):
            print("Contraseña válida.")
            break
        else:
            print("Contraseña no válida. Intente otra.")

    usuarios[nombre] = {"sexo": sexo, "contraseña": contraseña}
    print("Usuario ingresado con éxito!!")

def buscar_usuario():
    nombre = input("Ingrese usuario a buscar: ")
    if nombre in usuarios:
        datos = usuarios[nombre]
        print(f"El sexo del usuario es: {datos['sexo']} y la contraseña es: {datos['contraseña']}")
    else:
        print("El usuario no se encuentra.")

def eliminar_usuario():
    nombre = input("Ingrese usuario a eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado!")
    else:
        print("No se pudo eliminar usuario!")

def opc():
    while True:
        print("\nMENU PRINCIPAL de Usuarios ")
        print("1.- Ingresar usuario.")
        print("2.- Buscar usuario.")
        print("3.- Eliminar usuario.")
        print("4.- Salir.")
        opcion = input("Ingrese opción: ")

        match opcion:
            case "1":
                ingresar_usuario()
            case "2":
                buscar_usuario()
            case "3":
                eliminar_usuario()
            case "4":
                print("Saliendo del programa...")
                break
            case _:
                print("Debe seleccionar una opción válida.")

opc()
