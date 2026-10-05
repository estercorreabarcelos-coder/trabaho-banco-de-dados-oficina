def historico_precos():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    sql = """
        SELECT 
            hp.id,
            s.nome AS servico,
            hp.preco_antigo,
            hp.preco_novo,
            hp.data_alteracao
        FROM historico_precos hp
        INNER JOIN servicos s
            ON hp.servico_id = s.id
        ORDER BY hp.data_alteracao DESC
    """

cursor.execute(sql)

registros = cursor.fetchall()

print("\n===== HISTÓRICO DE PREÇOS =====")

for registro in registros:
    print(
        f"ID: {registro[0]} | "
        f"Produto: {registro[1]} | "
        f"Preço antigo: R$ {registro[2]:.2f} | "
        f"Preço novo: R$ {registro[3]:.2f} | "
        f"Data da alteração: {registro[4]}"
    )

    cursor.close()
    conexao.close()

def historico_status():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    sql = """
        SELECT
            hs.id,
            hs.ordem_id,
            hs.status_antigo,
            hs.status_novo,
            hs.data_alteracao
        FROM historico_status_ordem hs
        ORDER BY hs.data_alteracao DESC
    """

    cursor.execute(sql)

    registros = cursor.fetchall()

    print("\n===== HISTÓRICO DE STATUS DAS ORDENS =====")

    for registro in registros:
        print(
            f"ID: {registro[0]} | "
            f"Ordem ID: {registro[1]} | "
            f"Status antigo: {registro[2]} | "
            f"Status novo: {registro[3]} | "
            f"Data da alteração: {registro[4]}"
        )

    cursor.close()
    conexao.close()
