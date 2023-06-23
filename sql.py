import sqlite3
from sqlite3 import Error

# Función para abrir una conexión a la base de datos SQLite
def abrir_conexion():
    conexion = None
    try:
        conexion = sqlite3.connect("ip.db")
        print("Conexión a la base de datos SQLite exitosa.")
    except Error as e:
        print("Error al abrir la base de datos:", e)
    return conexion


def mostrar_contenido(conexion, consulta):
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta)
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)
    except Error as e:
        print("Error al ejecutar la consulta:", e)


conexion = abrir_conexion()
if conexion is not None:
    consulta = "SELECT * FROM ips"  # Reemplaza "acc" con el nombre de tu tabla
    mostrar_contenido(conexion, consulta)
    conexion.close()
