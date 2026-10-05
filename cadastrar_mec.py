from conexao import conectar

def cadastrar_mecanico():

    nome = input("Nome: ")
    cpf = input("CPF: ")
    especialidade = input("Especialidade: ")
    data_contratacao = input("Data de contratação (AAAA-MM-DD): ")

    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    sql = """
        INSERT INTO mecanicos
        (nome, cpf, especialidade, data_contratacao)
        VALUES (%s, %s, %s, %s)
    """

    valores = (
        nome,
        cpf,
        especialidade,
        data_contratacao
    )

    try:
        cursor.execute(sql, valores)
        conexao.commit()

        print("\nMecânico cadastrado com sucesso!")

    except Exception as erro:
        print("\nErro:", erro)

    finally:
        cursor.close()
        conexao.close()