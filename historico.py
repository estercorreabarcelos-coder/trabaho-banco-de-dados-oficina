historico = []


def registrar_alteracao(ordem_id, status_antigo, status_novo):
    alteracao = {
        "ordem_id": ordem_id,
        "status_antigo": status_antigo,
        "status_novo": status_novo
    }

    historico.append(alteracao)


def listar_historico():
    print("\n===== HISTÓRICO DE ALTERAÇÕES =====")

    if not historico:
        print("Nenhuma alteração registrada.")
        return

    for alteracao in historico:
        print(
            f"Ordem: {alteracao['ordem_id']} | "
            f"Status anterior: {alteracao['status_antigo']} | "
            f"Novo status: {alteracao['status_novo']}"
        )
