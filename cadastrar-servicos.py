from conexão import conectar 

def cadastrar_servicos():
    nome = input("Nome do serviço: ")
    descricao = input ("Descrição: ")
    preco = float(input("Preço: "))
    tempo_estimado = int(input("Tempo em minutos: "))

    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()
    sql = """
        INSERT INTO servicos
        (nome, descricao, preco, tempo_estimado)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            nome,descricao,preco,tempo_estimado
        ))
        conexao.commit()
        print("Serviço cadastrado!!")

    except Exception as erro:
        print("Deu erro: ",erro)

    finally:
        cursor.close()
        conexao.close()