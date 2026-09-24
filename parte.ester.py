import mysql.connector

def conectar():
    banco = mysql.connector.connect(
        host="localhost"
        user="root"
        passaword="Senac2026"
        database="oficina_carros"
    )
    return banco

from conexao import connectar 

def cadastrar_cliente():
    print("\n-----CADASTRAR CLIENTE----")

    nome = input("Nome: ")
    cpf =input("CPF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    banco = connectar()
    cursor = banco.cursor()

    sql = """
    INSERT INT clientes (nome, cpf, telefone, email)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (nome, cpf, telefone, email))