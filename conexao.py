import mysql.connector


def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Senac2026",
            database="oficina_carros"
        )

        return conexao

    except mysql.connector.Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
        return None