import os
import subprocess  # Módulo para ejecutar comandos del sistema


def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def ejecutar_script(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        print(f"\n--- Ejecutando {ruta_script} ---\n")
        # Ejecuta el script en un nuevo proceso
        subprocess.run(['python', ruta_script_absoluta], check=True)
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error al ejecutar el script: {e}")


def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        '2': 'Unidad 2/2.1. Estructuras de Datos/2.1-1. Ejemplo Estructuras de Datos.py',
        # Agrega más rutas según sea necesario
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código, ejecutarlo o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)

            # Pregunta al usuario si desea ejecutar el script
            ejecutar = input("¿Quieres ejecutar este script? (Sí/No): ").lower()
            if ejecutar == 'si' or ejecutar == 's':
                ejecutar_script(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    mostrar_menu()