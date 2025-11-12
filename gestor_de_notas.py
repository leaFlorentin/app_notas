import json
import os


RUTA = "notas.json"


#Carga el usuario si existen, de lo contrario retorna un array vacio
def cargar_usuario():
    if os.path.exists(RUTA):
        try:
            with open(RUTA, "r") as l:
                return json.load(l)
        except json.JSONDecodeError:
            return []

# Guarda el nuevo usuario creado en el json
def guardar_usuario(usuario):
    with open(RUTA, "w") as f:
        json.dump(usuario, f, indent=4)



#El usuario inicia sesion, con cuenta ya creada dentro del json
def iniciar_sesion(usuario):
    nombre = input("Digame su nombre de ususario: ")
    contraseña  = input("Digame su contraseña")

    if nombre in usuario and usuario [nombre][contraseña] == contraseña:
        print(f"Bienvenido {nombre} a tu bloc de notas")
    else:
        print("nombre o contraseña invalida")
        



#Crea un usuario nuevo, para luego guardarlo 
def crear_usuario(usuario):
    nombre = input("Ingresar el nombre que desea ponerse: ")
    if nombre in usuario : 
        print("El usuario aya esta en uso")
        return None
    contraseña = input("Ingrese una contraseña:" )
    usuario[nombre] = {"contraseña": contraseña, "nota":[]}
    guardar_usuario(usuario)
    print("Usuario creado!!!")
    return nombre



#Carga las notas si existen, de lo contrario retorna un array vacio
def cargar_notas():

    if os.path.exists(RUTA):
        try: 
            with open(RUTA, "r") as f:
                return json.load(f)
        except json.JSONDecodeError: 
            return []
    else: 
        return []



#Guarda las notas
def guardar_notas(notas):
    with open(RUTA, "w") as f:
        json.dump(notas, f, indent = 4 )




#Pide titulo y contenido para luego agragar al archivo de notas
def agregar_nota(notas):
    titulo = input("Dime el titulo que quieres colocarle: ")
    contenido = input("Contenido: ")
    contenido_agregado = {"titulo": titulo, "contenido": contenido}
    notas.append(contenido_agregado)
    guardar_notas(notas)


#Muestra todas las notas que contiene el archivo 
def mostrar_notas(notas):
    for nota in notas: 
        print("Titulo: ", nota["titulo"])
        print("Contenido: ", nota["contenido"])


#Elimina las notas que contiene el archivo, no asi el archivo
def eliminar_notas():

    confirmacion = input("Usted desea eliminar todas las notas? ").lower()

    if confirmacion == "si":
        with open("notas.json", "w") as f: 
            json.dump([], f, indent=4)
        print("Se han eliminado las notas anteriores.")
    else: 
        print("Operacion cancelada")


#Comienza el bucle para consultar sobre las opciones que desea realizar
while True:

    print("A- Iniciar sesion")
    print("B- Crear cuenta")
    print("C - Salir")
    
    opcion_elegida = int(input("Seleccione una opcion: ")).lower()
    usuario = cargar_usuario()

    if opcion_elegida == "a": 
        iniciar_sesion(usuario)
    elif opcion_elegida == "b":
        crear_usuario(usuario)
    elif opcion_elegida == "c": 
        print("Adios!")
        break
    else: 
        print("Opcion invalida")

""" 
    print("1- Agregar notas: ")
    print("2- Ver todas las notas ")
    print("3- Eliminar todas las notas ")
    print("4- Salir")

    opcion = int(input("Elige una opcion: "))
    notas = cargar_notas()
    if opcion == 4:
        print("Adios!!")
        break
    elif opcion == 1:
        agregar_nota(notas)
    elif opcion == 2: 
        mostrar_notas(notas)
    elif opcion == 3:
        eliminar_notas()
    else:
        print("Error")

"""