from conexao import conectar


def cadastrar_cliente():
    print("\n===== CADASTRAR CLIENTE =====")

    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("Email: ")

    banco = conectar()
    cursor = banco.cursor()

    sql = """
        INSERT INTO clientes
        (nome, cpf, email, data_cadastro)
        VALUES (%s, %s, %s, CURDATE())
    """

    try:
        cursor.execute(sql, (nome, cpf, email))
        banco.commit()
        print("Cliente cadastrado com sucesso!")

    except Exception as erro:
        print("Erro:", erro)

    finally:
        cursor.close()
        banco.close()


def listar_clientes():
    print("\n===== LISTA DE CLIENTES =====")

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    for cliente in clientes:
        print(cliente)

    cursor.close()
    banco.close()


def buscar_cliente():
    print("\n===== BUSCAR CLIENTE =====")

    id_cliente = input("Digite o ID do cliente: ")

    banco = conectar()
    cursor = banco.cursor()

    sql = """
        SELECT *
        FROM clientes
        WHERE id_cliente = %s
    """

    cursor.execute(sql, (id_cliente,))

    cliente = cursor.fetchone()

    if cliente:
        print(cliente)
    else:
        print("Cliente não encontrado.")

    cursor.close()
    banco.close()


def atualizar_cliente():
    print("\n===== ATUALIZAR CLIENTE =====")

    id_cliente = input("ID do cliente: ")
    nome = input("Novo nome: ")
    email = input("Novo email: ")

    banco = conectar()
    cursor = banco.cursor()

    sql = """
        UPDATE clientes
        SET nome = %s, email = %s
        WHERE id_cliente = %s
    """

    try:
        cursor.execute(sql, (nome, email, id_cliente))
        banco.commit()

        if cursor.rowcount > 0:
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")

    except Exception as erro:
        print("Erro:", erro)

    finally:
        cursor.close()
        banco.close()


def excluir_cliente():
    print("\n===== EXCLUIR CLIENTE =====")

    id_cliente = input("ID do cliente: ")

    banco = conectar()
    cursor = banco.cursor()

    sql = """
        DELETE FROM clientes
        WHERE id_cliente = %s
    """

    try:
        cursor.execute(sql, (id_cliente,))
        banco.commit()

        if cursor.rowcount > 0:
            print("Cliente excluído com sucesso!")
        else:
            print("Cliente não encontrado.")

    except Exception as erro:
        print("Erro:", erro)

    finally:
        cursor.close()
        banco.close()