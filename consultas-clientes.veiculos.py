def consulta_clientes_veiculos(clientes, veiculos):
    print("\n===== CLIENTES E VEÍCULOS =====")

    for cliente in clientes:

        for veiculo in veiculos:

            if veiculo["cliente_id"] == cliente["id"]:

                print(
                    f"Cliente: {cliente['nome']} | "
                    f"Veículo: {veiculo['marca']} {veiculo['modelo']} | "
                    f"Placa: {veiculo['placa']}"
                )