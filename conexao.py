import mysql.connector


def conectar():
    banco = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SUA_SENHA",
        database="oficina"
    )

    return banco