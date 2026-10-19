from conexao import conectar

def consultar_servicos():
    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    print("\n===== CONSULTAS DE SERVIÇOS =====")
    print("1 - Serviços acima de R$ 500")
    print("2 - Serviços entre R$ 100 e R$ 500")
    print("3 - Cinco serviços mais caros")

    opcao = input("Escolha: ")

    try:
        if opcao == "1":
            sql = """
                SELECT nome, preco
                FROM servicos
                WHERE preco > 500
                ORDER BY preco DESC
            """

        elif opcao == "2":
            sql = """
                SELECT nome, preco
                FROM servicos
                WHERE preco BETWEEN 100 AND 500
                ORDER BY preco
            """

        elif opcao == "3":
            sql = """
                SELECT nome, preco
                FROM servicos
                ORDER BY preco DESC
                LIMIT 5
            """

        else:
            print("Opção inválida.")
            return

        cursor.execute(sql)
        resultados = cursor.fetchall()

        print("\n===== RESULTADOS =====")

        for resultado in resultados:
            print(f"Serviço: {resultado[0]} | Preço: R$ {resultado[1]:.2f}")

    except Exception as erro:
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()