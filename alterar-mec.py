from conexao import conectar

def atualizar_mecanicos():
    id_mecanico = input("ID do mêcanico: ")
    nome = input("Novo nome: ")
    especialidade = input("Nova especialidade: ")
    
    conexao = conectar()

    if conexao is None:
        return
    cursor = conexao.cursor()

    sql = """
        UPDATE mecanicos
        SET nome = %s,
            especialidade = %s
        WHERE id_mecanico = %s
    """
    valores = (
        nome,
        especialidade,
        id_mecanico
    )
    try :
        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            print("\n Mecânico atualizado")

        else:
            print("\n Mecanico não encontrado")

    except Exception as erro:
        print("Deu erro", erro )

    finally:
        cursor.close()
        conexao.close()