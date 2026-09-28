import mysql.connector


def conectar():
    banco = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Senac2026",
        database="oficina_carros"
    )

    return banco