from conexao import conectar

def listar_servicos():
    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    sql = """
        SELECT
            id_servico,
            nome,
            descricao,
            preco,
            tempo_estimado,
            status
        FROM servicos
        ORDER BY nome
    """

    try:

        cursor.execute(sql)

        servicos = cursor.fetchall()

        print("\n===== SERVIÇOS =====")

        for servico in servicos:

            print(
                f"ID: {servico[0]} | "
                f"{servico[1]} | "
                f"R$ {servico[3]:.2f} | "
                f"{servico[4]} minutos | "
                f"{servico[5]}"
            )

    except Exception as erro:

        print("Erro:", erro)

    finally:

        cursor.close()
        conexao.close()