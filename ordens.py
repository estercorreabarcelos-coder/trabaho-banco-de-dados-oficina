import mysql.connector

def conectar():
    try:
        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Senac2026",
            database="oficina_carros"
        )
        return banco

    except mysql.connector.Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
        return None


# Abre uma nova ordem de serviço
def abrir_ordem():
    banco = conectar()

    if banco is None:
        return

    cursor = banco.cursor()

    cliente = int(input("ID do cliente: "))
    veiculo = int(input("ID do veículo: "))
    mecanico = int(input("ID do mecânico: "))
    observacoes = input("Observações: ")

    sql = """
    INSERT INTO ordens_servico
    (id_cliente, id_veiculo, id_mecanico, observacoes)
    VALUES (%s, %s, %s, %s)
    """

    valores = (cliente, veiculo, mecanico, observacoes)

    cursor.execute(sql, valores)
    banco.commit()

    print("Ordem aberta com sucesso!")

    cursor.close()
    banco.close()


# Adiciona um serviço em uma ordem
def adicionar_servico():
    banco = conectar()

    if banco is None:
        return

    cursor = banco.cursor()

    ordem = int(input("ID da ordem: "))
    servico = int(input("ID do serviço: "))
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço do serviço: "))

    sql = """
    INSERT INTO itens_servico
    (id_ordem, id_servico, quantidade, preco_unitario)
    VALUES (%s, %s, %s, %s)
    """

    valores = (ordem, servico, quantidade, preco)

    cursor.execute(sql, valores)
    banco.commit()

    print("Serviço adicionado!")

    cursor.close()
    banco.close()


# Mostra as ordens cadastradas
def consultar_ordens():
    banco = conectar()

    if banco is None:
        return

    cursor = banco.cursor()

    sql = """
    SELECT
        os.id_ordem,
        c.nome,
        v.modelo,
        m.nome,
        os.status
    FROM ordens_servico os
    INNER JOIN clientes c
        ON os.id_cliente = c.id_cliente
    INNER JOIN veiculos v
        ON os.id_veiculo = v.id_veiculo
    INNER JOIN mecanicos m
        ON os.id_mecanico = m.id_mecanico
    """

    cursor.execute(sql)
    ordens = cursor.fetchall()

    for ordem in ordens:
        print(ordem)

    cursor.close()
    banco.close()


# Altera o status da ordem
def alterar_status():
    banco = conectar()

    if banco is None:
        return

    cursor = banco.cursor()

    ordem = int(input("ID da ordem: "))
    status = input("Novo status: ")

    sql = """
    UPDATE ordens_servico
    SET status = %s
    WHERE id_ordem = %s
    """

    valores = (status, ordem)

    cursor.execute(sql, valores)
    banco.commit()

    if cursor.rowcount > 0:
        print("Status alterado!")
    else:
        print("Ordem não encontrada.")

    cursor.close()
    banco.close()