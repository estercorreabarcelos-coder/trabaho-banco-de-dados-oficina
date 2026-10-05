def relatorio_ordens():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    sql = """
        SELECT
            o.id,
            c.nome AS cliente_nome,
            v.marca AS veiculo_marca,
            v.modelo AS veiculo_modelo,
            v.placa AS veiculo_placa,
            o.data_abertura,
            o.data_fechamento,
            o.status
        FROM ordens_servico os

        INNER JOIN clientes c 
            ON o.cliente_id = c.id
        
        INNER JOIN veiculos v 
            ON o.veiculo_id = v.id

        INNER JOIN mecanicos m
            ON o.mecanico_id = m.id
        
        ORDER BY o.data_abertura DESC
    """

    cursor.execute(sql)

    registros = cursor.fetchall()

    print("\n===== RELATÓRIO DE ORDENS =====")

    for registro in registros:
        print(
            f"ID: {registro[0]} | "
            f"Cliente: {registro[1]} | "
            f"Veículo: {registro[2]} {registro[3]} | "
            f"Data de abertura: {registro[4]} | "
            f"Data de fechamento: {registro[5]} | "
            f"Status: {registro[6]} | "
            f"Mecanico: {registro[7]}"
        )

    cursor.close()
    conexao.close()