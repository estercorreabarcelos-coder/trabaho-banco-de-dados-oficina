from conexão import conectar

def excluir_mecanico():

    id_mecanico = input("ID do mecânico que voce quer excluir: ")

    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    sql = """
        DELETE FROM mecanicos
        WHERE id_mecanico = %s
    """

    try:

        cursor.execute(sql, (id_mecanico,))

        conexao.commit()

        if cursor.rowcount > 0:
            print("\nMecânico excluído!")

        else:
            print("\nMecânico não encontrado.")

    except Exception as erro:

        print("\nNão foi possível excluir.")
        print("Motivo: ", erro)

    finally:

        cursor.close()
        conexao.close()