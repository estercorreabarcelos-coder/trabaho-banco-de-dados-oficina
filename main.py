from cliente import (
   cadastrar_cliente,
   listar_clientes,
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
   print("0 - Sair")
   opcao = input("\nEscolha uma opção: ")
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
   elif opcao == "0":
       print("Programa encerrado!")
       break
   else:
       print("Opção inválida!")