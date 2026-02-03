import json
import pickle
import os

ARCHIVO_FORMATO = "formato.txt"
ARCHIVO_JSON = "tareas.json"
ARCHIVO_PKL = "tareas.pckl"


def cargar_tareas(formato):
    if formato == "json":
        if os.path.exists(ARCHIVO_JSON):
            with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
    else:
        if os.path.exists(ARCHIVO_PKL):
            with open(ARCHIVO_PKL, "rb") as f:
                return pickle.load(f)
    return []


def guardar_tareas(tareas, formato):
    if formato == "json":
        with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(tareas, f, indent=4)
    else:
        with open(ARCHIVO_PKL, "wb") as f:
            pickle.dump(tareas, f)


def agregar_tarea(tareas, formato):
    nombre = input("Nombre de la tarea: ")
    fecha = input("Fecha límite (YYYY-MM-DD): ")

    tarea = {
        "nombre": nombre,
        "fecha_limite": fecha,
        "estado": "pendiente"
    }

    tareas.append(tarea)
    guardar_tareas(tareas, formato)


def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas")
        return

    for i, tarea in enumerate(tareas):
        print(f"{i + 1}. {tarea['nombre']} | {tarea['fecha_limite']} | {tarea['estado']}")


def modificar_estado(tareas, formato):
    listar_tareas(tareas)
    num = int(input("Número de tarea a completar: ")) - 1

    if 0 <= num < len(tareas):
        tareas[num]["estado"] = "completada"
        guardar_tareas(tareas, formato)
    else:
        print("Número incorrecto")


def eliminar_tarea(tareas, formato):
    listar_tareas(tareas)
    num = int(input("Número de tarea a eliminar: ")) - 1

    if 0 <= num < len(tareas):
        if tareas[num]["estado"] == "completada":
            tareas.pop(num)
            guardar_tareas(tareas, formato)
        else:
            print("La tarea no está completada")
    else:
        print("Número incorrecto")


def cambiar_formato(formato_actual, tareas):
    print(f"Formato actual: {formato_actual}")
    nuevo = "pckl" if formato_actual == "json" else "json"

    resp = input(f"¿Cambiar a {nuevo}? (s/n): ").lower()
    if resp == "s":
        guardar_tareas(tareas, nuevo)
        with open(ARCHIVO_FORMATO, "w") as f:
            f.write(nuevo)
        exit()


def elegir_formato():
    if os.path.exists(ARCHIVO_FORMATO):
        with open(ARCHIVO_FORMATO, "r") as f:
            return f.read()

    while True:
        formato = input("Elige formato (json / pckl): ").lower()
        if formato in ["json", "pckl"]:
            with open(ARCHIVO_FORMATO, "w") as f:
                f.write(formato)
            return formato
        print("Formato no válido")


def menu():
    print("""
1. Agregar tarea
2. Modificar estado de tarea
3. Eliminar tarea
4. Listar tareas
5. Cambiar formato de serialización
0. Salir
""")

def main():
    formato = elegir_formato()
    tareas = cargar_tareas(formato)

    while True:
        menu()
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                agregar_tarea(tareas, formato)
            case "2":
                modificar_estado(tareas, formato)
            case "3":
                eliminar_tarea(tareas, formato)
            case "4":
                listar_tareas(tareas)
            case "5":
                cambiar_formato(formato, tareas)
            case "0":
                break
            case _:
                print("Opción no válida")

if __name__ == "__main__":
    main()
