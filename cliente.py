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

    banco.commit()

    print("Cliente cadastrado com sucesso!")

    cursor.close()
    banco.close()

def listar_clientes():
    print("\n ---- LISTA DE CLIENTES----")

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    for cliente in clientes:
        print(cliente)

    cursor.close()
    banco.close()

def atualizar_cliente():
    print("\n ---- ATUALIZAR CLIENTE------")

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    for cliente in clientes:
        print(cliente)

    cursor.close()
    banco.close()

def atualizar_cliente():
    print("\n ------ATUALIZAR CLIENTE------")

    id_cliente = input("Digite o ID do cliente: ")
    telefone = input("Novo telefone: ")
    email = input("Novo email: ")

    banco = conectar()
    cursor = banco.cursor()

    sql = """
    UPDATE clientes
    SET telefone = %s, email = %s
    WHERE id_cliente = %s
    """

    cursor.execute(sql, (telefone, email, id_cliente))

    banco.commit()

    print(" Cliente atualizado com sucesso!")

    cursor.close()
    banco.close()

def excluir_cliente():
    print("\n -----EXCLUIR CLIENTE-----")

    id_cliente = input("Digite o ID do cliente: ")

    banco = conectar()
    cursor = banco.cursor()

    sql = """
    DELETE FROM clientes
    WHERE id_cliente = %s
    """

    cursor.eexecute( sql, (id_cliente,))

    banco.commit()

    print("Cliente excluido co sucesso!")

    cursor.close()
    banco.close()

def burcar_cliente():
    print("\n ---- BUSCAR CLIENTE-----")

    nome = input("Digite uma parte do nome: ")

    banco = conectar()
    cursor = banco.cursor()

    sql = """
    SELECT *
    FROM clientes
    WHERE nome LIKE %s
    ORDER BY nome
    """

    cursor.execute(sql, ( "%" + nome + "%", ))

    clientes = cursor.fetchall()

    for cliente in clientes:
        print(cliente)

    cursor.close()
    banco.close()


