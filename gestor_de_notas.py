import json
import os

RUTA = "notas.json"

def cargar_notas():

    if os.path.exists(RUTA):
        try: 
            with open(RUTA, "r") as f:
                return json.load(f)
        except json.JSONDecodeError: 
            return []
    else: 
        return []


def guardar_notas(notas):
    with open(RUTA, "w") as f:
        json.dump(notas, f, indent = 4 )

def agregar_nota(notas):
    titulo = input("Dime el titulo que quieres colocarle: ")
    contenido = input("Contenido: ")
    contenido_agregado = {"titulo": titulo, "contenido": contenido}
    notas.append(contenido_agregado)
    guardar_notas(notas)

def mostrar_notas(notas):
    for nota in notas: 
        print("Titulo: ", nota["titulo"])
        print("Contenido: ", nota["contenido"])

def eliminar_notas():

    confirmacion = input("Usted desea eliminar todas las notas? ").lower()

    if confirmacion == "si":
        with open("notas.json", "w") as f: 
            json.dump([], f, indent=4)
        print("Se han eliminado las notas anteriores.")
    else: 
        print("Operacion cancelada")

while True:
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