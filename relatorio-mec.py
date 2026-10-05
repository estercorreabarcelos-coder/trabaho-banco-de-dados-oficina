def relatorio_mecanicos(mecanicos, ordens):
    print("\n===== RELATÓRIO DOS MECÂNICOS =====")

    for mecanico in mecanicos:

        quantidade_ordens = 0
        valor_total = 0

        for ordem in ordens:

            if ordem["mecanico_id"] == mecanico["id"]:

                quantidade_ordens += 1
                valor_total += ordem["valor"]

        print(
            f"Mecânico: {mecanico['nome']} | "
            f"Ordens realizadas: {quantidade_ordens} | "
            f"Valor dos serviços: R$ {valor_total:.2f}"
        )