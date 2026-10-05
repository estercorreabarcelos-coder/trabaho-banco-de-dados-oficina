def relatorio_ordens(ordens):
    print("\n===== RELATÓRIO DE ORDENS DE SERVIÇO =====")

    if not ordens:
        print("Nenhuma ordem cadastrada.")
        return

    for ordem in ordens:
        print(
            f"Ordem: {ordem['id']} | "
            f"Cliente: {ordem['cliente']} | "
            f"Veículo: {ordem['veiculo']} | "
            f"Mecânico: {ordem['mecanico']} | "
            f"Status: {ordem['status']} | "
            f"Valor: R$ {ordem['valor']:.2f}"
        )