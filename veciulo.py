from conexao import conectar

def cadastrar_veiculo():
    print("\n ----- CADASTRAR VEÍCULO-----")

    id_cliente = input("ID do cliente: ")
    placa = input("Placa: ")
    marca = input(" Marca: ")
    modelo = input(" Modelo: ")
    ano = input (" Ano: ")

    banco = conectar()
    cursor = banco.cursor()

    sql = """
    INSERT INTO veiculos
    (id_cliente, placa, marca, modelo, ano)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(
        sql,
        (id_cliente, placa, marca, modelo, ano)
    )

    banco.commit()

    print("Veículo cadastrado com sucesso!")

    cursor.close()
    banco.close()

def listar_veiculos():
    print("\n ----- LISTA DE VEÍCULOS-----")

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM veiculos")

    veiculos = cursor.fetchall()

    for veiculo in veiculos:
        print(veiculo)

    cursor.close()
    banco.close()


def busar_veiculos_clientes():
    print("\n -----VEÍCULO DO CLIENTE-----")

    id_cliene = input("Digite o ID do cliente: ")

    banco = conectar()
    cursor = banco.cursor()

    sql = """
    SELECT 
        clientes.nome
        veiculos.placa
        veiculos.marca
        veiculos.modelo
        veiculos.ano
    FROM clientes
    INNER JOIN veiculos
        ON clientes.id_cliente = veiculos.id_cliente
    WHERE clientes.id_cliente = %s
    """

    cursor.execute(sql, (id_cliente,))

    veiculos = cursor.fetchall()

    for veiculo in veiculos:
        print(veiculo)


    cursor.close()
    banco.close()

def atualizar_veiculo():
    print("\n ------ATUALIZAR VEÍCULO-----")

    id_veiculo = input("ID do veículo: ")
    modelo = input(" Novo modelo: ")
    ano = input("Novo ano: ")

    banco = conectar()
    cursor = banco.cursor()

    sql = """
    UPDATE veiculos
    SET moelo = %s, ano = %s
    WHERE id_veiculo = %s
    """

    cursor.execute(sql, (modelo, ano, id_veiculo))

    banco.commit()

    print(" Veículo atualizado com sucesso!")

    cursor.close()
    banco.close()