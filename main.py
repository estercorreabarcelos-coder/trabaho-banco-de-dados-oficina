from cliente import (
    cadastrar_cliente,
    listar_cliente,
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

from consulta_servico import (
    consultar_servicos_por_nome,
    consultar_servicos_por_preco
)


while True:


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

