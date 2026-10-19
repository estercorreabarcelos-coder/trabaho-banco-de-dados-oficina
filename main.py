from cliente import (
   cadastrar_cliente,
   listar_cliente,
   atualizar_cliente,
   excluir_cliente,
   buscar_cliente
)
from veiculo import (
   cadastrar_veiculo,
   listar_veiculos,
   buscar_veiculos_cliente,
   atualizar_veiculo
)
from consultas_clientes_veiculos import consulta_clientes_veiculos
from historico import (
    registrar_alteracao,
    listar_historico
)

from relatorios import *
from consultas_valoresgastos import *
from relatorio_mec import *

while True:
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