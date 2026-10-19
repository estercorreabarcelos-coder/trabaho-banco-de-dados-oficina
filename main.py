
from cliente import (
    cadastrar_cliente,
    listar_clientes,
    atualizar_cliente,
    excluir_cliente,
    buscar_cliente
)
from consultas_clientes_veiculos import consulta_clientes_veiculos
from historico import (
    registrar_alteracao,
    listar_historico
)

from relatorios import *
from consultas_valoresgastos import *
from relatorio_mec import *

from veiculo import (
    cadastrar_veiculo,
    listar_veiculos,
    buscar_veiculos_cliente,
    atualizar_veiculo
)

from cadastrar_mec import cadastrar_mecanico
from listar_mec import listar_mecanicos
from cadastrar_servicos import cadastrar_servicos
from listra_servicos import listar_servicos
from alterar_preco import alterar_preco

from consulta_ser import (
    consultar_servicos_por_nome,
    consultar_servicos_por_preco
)


while True:
<<<<<<< HEAD
   print("\n==============================")
   print("       OFICINA DE CARROS")
   print("==============================")
   print("1 - Cadastrar cliente")
   print("2 - Listar clientes")
   print("3 - Atualizar cliente")
   print("4 - Excluir cliente")
   print("5 - Buscar cliente")
   print("6 - Cadastrar veículo")
   print("7 - Listar veículos")
   print("8 - Buscar veículos de um cliente")
   print("9 - Atualizar veículo")
   print("10 - Consultar clientes e veículos")
   print("11 - Valores gastos")
   print("12 - Histórico de alterações")
   print("13 - Listar histórico de alterações")
   print("14 - Histórico de preços")
   print("15 - Histórico de status")
   print("16 - Relatório de mecânicos")
   print("17 - Relatório de ordens")
   print("0 - Sair")
   opcao = input("\nEscolha uma opção: ")
   if opcao == "1":
       cadastrar_cliente()
   elif opcao == "2":
       listar_cliente()
   elif opcao == "3":
       atualizar_cliente()
   elif opcao == "4":
       excluir_cliente()
   elif opcao == "5":
       buscar_cliente()
   elif opcao == "6":
       cadastrar_veiculo()
   elif opcao == "7":
       listar_veiculos()
   elif opcao == "8":
       buscar_veiculos_cliente()
   elif opcao == "9":
       atualizar_veiculo()      
   elif opcao == "10":
       consulta_clientes_veiculos()
   elif opcao == "11":
       valores_gastos()
   elif opcao == "12":
       registrar_alteracao()
   elif opcao == "13":
       listar_historico()
   elif opcao == "14":
       relatorio_mecanicos()
   elif opcao == "15":
         relatorio_ordens()
   elif opcao == "0":
       print("Programa encerrado!")
       break
   else:
       print("Opção inválida!")
=======
    print("\n====================================")
    print("          OFICINA DE CARROS")
    print("====================================")
    print("\n--- CLIENTES ---")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Atualizar cliente")
    print("4 - Excluir cliente")
    print("5 - Buscar cliente")

    print("\n--- VEÍCULOS ---")
    print("6 - Cadastrar veículo")
    print("7 - Listar veículos")
    print("8 - Buscar veículos de um cliente")
    print("9 - Atualizar veículo")

    print("\n--- MECÂNICOS ---")
    print("10 - Cadastrar mecânico")
    print("11 - Listar mecânicos")

    print("\n--- SERVIÇOS ---")
    print("12 - Cadastrar serviço")
    print("13 - Listar serviços")
    print("14 - Alterar preço de serviço")
    print("15 - Consultar serviço por nome")
    print("16 - Consultar serviços por faixa de preço")

    print("\n0 - Sair")
    print("====================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        atualizar_cliente()
    elif opcao == "4":
        excluir_cliente()
    elif opcao == "5":
        buscar_cliente()
    elif opcao == "6":
        cadastrar_veiculo()
    elif opcao == "7":
        listar_veiculos()
    elif opcao == "8":
        buscar_veiculos_cliente()
    elif opcao == "9":
        atualizar_veiculo()
    elif opcao == "10":
        cadastrar_mecanico()
    elif opcao == "11":
        listar_mecanicos()
    elif opcao == "12":
        cadastrar_servicos()
    elif opcao == "13":
        listar_servicos()
    elif opcao == "14":
        alterar_preco()
    elif opcao == "15":
        consultar_servicos_por_nome()
    elif opcao == "16":
        consultar_servicos_por_preco()
    elif opcao == "0":
        print("Sistema encerrado!")
        break
    else:
        print("Opção inválida! Tente novamente.")
>>>>>>> d1651e8aa37ee7e9d8624de4bf6cbffe987ca0a0
