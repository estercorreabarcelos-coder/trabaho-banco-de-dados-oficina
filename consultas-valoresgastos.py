def valores_gastos(clientes, ordens):
    print("\n===== VALORES GASTOS PELOS CLIENTES =====")

    for cliente in clientes:

        total = 0

        for ordem in ordens:

            if ordem["cliente_id"] == cliente["id"]:
                total += ordem["valor"]

        print(
            f"Cliente: {cliente['nome']} | "
            f"Total gasto: R$ {total:.2f}"
        )