from conexão import conectar 

def alterar_preço():
    id_serviço = input("Digite o ID do serviço: ")
    novo_preço = float(input("Novo preço:").replace(",","."))

    conexao = conectar()
    
    if conexao is None:
        return

    cursor = conexao.cursor()
    sql = """
        UPDATE servicos
        SET preco = %s
        WHERE id_servico = %s
    """
    valores = (novo_preço, id_serviço)

    try:
        cursor.execute(sql,valores)
        conexao.commit()

        if cursor.rowcount >0:
            print("Preço atualizado com sucesso!!")
        else:
            print