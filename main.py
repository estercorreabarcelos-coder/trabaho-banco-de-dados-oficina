from cadastrar_mec import cadastrar_mec
from listar_mec import listar_mecanicos
from alterar_mec import alterar_mecanico
from excluir_mec import excluir_mecanico

from cadastrar_servicos import cadastrar_servicos
from listra_servicos import listra_servicos
from alterar_preco import alterar_preco
from consulta_ser import consulta_ser

while True:

    print("\n===== SISTEMA DA OFICINA =====")
    print("1 - Cadastrar mecânico")
    print("2 - Listar mecânicos")
    print("3 - Alterar mecânico")
    print("4 - Excluir mecânico")
    print("5 - Cadastrar serviço")
    print("6 - Listar serviços")
    print("7 - Alterar preço de serviço")
    print("8 - Consultar serviços")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_mec()

    elif opcao == "2":
        listar_mecanicos()

    elif opcao == "3":
        alterar_mecanico()

    elif opcao == "4":
        excluir_mecanico()

    elif opcao == "5":
        cadastrar_servicos()

    elif opcao == "6":
        listra_servicos()

    elif opcao == "7":
        alterar_preco()

    elif opcao == "8":
        consulta_ser()

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")