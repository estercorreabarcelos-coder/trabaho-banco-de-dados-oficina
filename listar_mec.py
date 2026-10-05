from conexao import conectar

def listar_mecanicos():
    conexao = conectar ()

    if conexao is None:
        return

    cursor = conexao.cursor()
    sql = """
        SELECT
            id_mecanico,
            nome,
            cpf,
            especialidade,
            data_contratacao,
            status
        FROM mecanicos
        ORDER BY nome
    """

    try:
        cursor.execute(sql)
        mecanicos = cursor.fetchall()
        print("\n===== MECÂNICOS =====")

        for mecanico in mecanicos:

            print(
                f"ID: {mecanico[0]} | "
                f"Nome: {mecanico[1]} | "
                f"CPF: {mecanico[2]} | "
                f"Especialidade: {mecanico[3]} | "
                f"Data: {mecanico[4]} | "
                f"Status: {mecanico[5]}"
            )

    except Exception as erro:

        print("Erro:", erro)

    finally:

        cursor.close()
        conexao.close()
