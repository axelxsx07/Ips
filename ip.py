import requests
import sqlite3



def obtener_ip_publica():
    try:
        response = requests.get('https://httpbin.org/ip')
        data = response.json()
        ip_publica = data['origin']
        return ip_publica
    except requests.exceptions.RequestException:
        return None

ip = obtener_ip_publica()


# Conectarse a la base de datos
conexion = sqlite3.connect('ip.db')
cursor = conexion.cursor()

# Crear tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS ips (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ip TEXT)''')


cursor.execute('INSERT INTO ips (ip) VALUES (?)', (ip,))
conexion.commit()


conexion.close()
