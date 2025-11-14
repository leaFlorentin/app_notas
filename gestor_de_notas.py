import json
import os

BASE_USUARIOS = "bloc_notas.json"


def base_de_usuarios():

# La funcion comprueba si ya existe el json y lo lee, de lo contrario crea el json con un diccionario vacio

    if os.path.exists(BASE_USUARIOS): 
        try: 
            with open(BASE_USUARIOS, "r") as f: 
                return json.load(f) 
        except json.JSONDecodeError: 
            return {}
    else: return {}



def guardar_usuarios(usuarios):
#Guarda el diccionario completo de usuarios en el archivo json 
    with open (BASE_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)



def escribir_notas(nombre):
#El usuario escribe nuevas notas y la guarda en su lista

    usuarios = base_de_usuarios()
    if nombre not in usuarios:
        print("Error: usuario no existe")
        return
    
    titulo = input("Título de la nota: ")
    contenido = input("Contenido de la nota: ")

    # Añadir nota a la lista
    usuarios[nombre]["notas"].append({
        "titulo": titulo,
        "contenido": contenido
    })

    guardar_usuarios(usuarios)



def leer_notas(nombre):
#Imprime / lee las notas del usuario guardadas

    usuarios = base_de_usuarios()
    if nombre not in usuarios:
        print("Error: usuario no existe")
        return

    notas = usuarios[nombre].get("notas", [])
    if not notas:
        print("No tienes notas guardadas")
        return

    for i, nota in enumerate(notas, 1):
        print(f"\nNota {i}")
        print("Título:", nota["titulo"])
        print("Contenido:", nota["contenido"])


def eliminar_notas(nombre):
#Borra/ elimina las notas del usuario y guarda el cambio

    usuarios = base_de_usuarios()

    if nombre not in usuarios:
        print("Error: usuario no existe")
        return
    
    usuarios[nombre]["notas"] = []

    guardar_usuarios(usuarios)
    print("Notas eliminadas.")


def menu_de_operaciones(nombre):

    while True :
        print("1 - Escribir nota")
        print("2- Ver mis notas")
        print("3 - Eliminar mis notas")
        print("4 - Salir")

        try: 
            operacion_elegida = int(input("Elige la operacion que quiera realizar: "))
        except: 
            print("Tienes que colocar un numero")

        if operacion_elegida == 4: 
            print("Adios ")
            break
        elif operacion_elegida == 1:
            escribir_notas(nombre)
        elif operacion_elegida == 2:
            leer_notas(nombre)
        elif operacion_elegida == 3:
            eliminar_notas(nombre)
        else:
            print("Opcion invalida")
            continue



def guardar_usuario_nuevo(nombre, contr):
#Crea un nuevo usuario en la base de datos con contraseña y lista vacia de notas

    usuarios = base_de_usuarios()   # Cargar usuarios existentes
    # Crear estructura del nuevo usuario
    usuarios[nombre] = {
        "contra": contr,
        "notas": []
    }

    # Guardar el JSON actualizado
    with open(BASE_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

    print("Usuario creado correctamente:", nombre)
    menu_de_operaciones(nombre)



def crear_cuenta():
# Permite al usuario crear una nueva cuenta

    nombre = input("Digame el nombre que quiere colocarse")
    contr = int(input("Digame la contraseña que quiere colocarse, debe ser numérica"))

    if nombre not in base_de_usuarios():
        guardar_usuario_nuevo(nombre, contr)
    else:
        print("El nombre ya esta en uso!")



def iniciar_sesion():
#Inciar sesion verificando nombre y contraseña en el archivo JSON

    usuarios = base_de_usuarios()   # Cargar usuarios existentes
    nombre = input("Digame su nombre de usuario")
    contr = int (input("Digame su contraseña"))

    if nombre in usuarios and usuarios[nombre]["contra"] == contr:
        print(f"Bienvenido {nombre} a su bloc de notas")
        menu_de_operaciones(nombre)
    else: 
        print("Nombre o contraseña incorrecta!!")


def main():


    while True: 
        print("Bienvenido a bloc de notas \n")
        print("A- Iniciar sesion")
        print("B- Crear cuenta")
        print("C- Salir")

        opcion_elegida = input("Eliga una opcion: ").lower()

        if opcion_elegida == "c":
            print("Hasta luego!")
            break
        elif opcion_elegida == "a":
            iniciar_sesion()
        elif opcion_elegida == "b":
            crear_cuenta()
        else:
            print("Opcion incorrecta")
            continue

print(main())