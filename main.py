import pyodbc
import config
import db
import repositorio

autenticado = False

while not autenticado:
   print("Criando string de conexão. Digite suas credenciais:")

   config.usuario = input("Usuário SQL Server: ").strip()
   config.senha = input("Senha SQL Server: ").strip()

   try:
      dados = db.testar_conexao()
      autenticado = True

      print("\nConexão realizada com sucesso!")
      print(f"Servidor: {dados['servidor']}")
      print(f"Banco: {dados['banco']}")
      print(f"Versão: {dados['versao']}")

   except pyodbc.Error as erro:
      print("\nFalha na conexão. Verifique usuário e senha.")

print("\nAcesso liberado para o menu principal.")

opcao = input(
   "Digite uma opção:\n"
   "[1] Etapa 1 - Testar conexão\n"
   "[2] Etapa 2 - CRUD de tutor\n"
   "[3] Etapa 3 - Relacionamento 1:N tutor → pet\n"
   "[4] Etapa 4 - Relacionamento N:N consulta ↔ procedimento\n"
   "[5] Bônus\n"
   "[sair] para finalizar \n"
   "Opção: "
) 

while opcao != "sair":
   if autenticado == False:
      print("Criando string de conceção digite: ")

      config.usuario = input("Usuário SQL Server: ").strip()
      config.senha = input("Senha SQL Server: ").strip()
   
   # questão 1
   if opcao == "1":
      try:
         dados = db.testar_conexao()

         print("\nConexão realizada com sucesso!")
         print(f"Servidor: {dados['servidor']}")
         print(f"Banco: {dados['banco']}")
         print(f"Versão: {dados['versao']}")

      except pyodbc.Error as erro:
         print(f"\nFalha na conexão: Usuario ou senha incorretos \n {erro}")

   # questão 2
   elif opcao == "2":
      print("\n")

      opcao_dois =input(
               " Digite uma opção: \n" \
               " [1] Create: criar_tutor \n" \
               " [2] Read: buscar tutor por ID \n" \
               " [3] Read: listar tutores \n"\
               " [4] Update: atualizar_tutor \n" \
               " [5] Delete: excluir_tutor \n"
               " Opção: " )

      if opcao_dois == "1":
         print("\n")

         id_tutor = repositorio.criar_tutor()
         if id_tutor is not None:
            print(f"Tutor cadastrado com sucesso! ID: {id_tutor}")

      elif opcao_dois == "2":
         print("\n")
         tutor = repositorio.buscar_tutor()

         if tutor == None:
            pass  
         else:
            print(tutor)
         
      elif opcao_dois == "3":
         print("\n")
         filtro = input("Digite um nome para filtrar (Enter para listar todos): ")

         tutores = repositorio.listar_tutores(filtro)

         if tutores:
            for tutor in tutores:
               print(tutor)
         else:
            print("Nenhum tutor encontrado.")

      elif opcao_dois == "4":
         print("\n")
         repositorio.atualizar_tutor(id_tutor = input("Digite o ID do tutor: "),
                         nome = input("Digite o nome do tutor: "),
                         email = input("Digite o email do tutor: "),
                         telefone = input("Digite o telefone do tutor: "),
                         cpf = input("Digite o cpf"))

      elif opcao_dois == "5":
         print("\n")
         repositorio.excluir_tutor()

      else: 
         print("\n")
         print("opção invalida")
   
   # questão 3
   elif opcao == "3":
      print("\n")
      
      opcao_tres = input(
                     " Digite uma opção: \n" \
                     " [1] criar pet \n" \
                     " [2] atualizar peso pet \n" \
                     " [3] transferir pet \n"\
                     " [4] excluir pet \n" \
                     " [5] listar pets do tutor \n" \
                     " [6] buscar pet com tutor \n" \
                     " Opção: " )
      
      if opcao_tres == "1":
         print("\n")
         repositorio.criar_pet()

      elif opcao_tres == "2":
         print("\n")
         repositorio.atualizar_peso_pet()

      elif opcao_tres == "3":
         print("\n")
         repositorio.transferir_pet()

      elif opcao_tres == "4":
         print("\n")
         repositorio.excluir_pet()

      elif opcao_tres == "5":
         print("\n")
         repositorio.listar_pets_do_tutor()

      elif opcao_tres == "6":
         print("\n")
         repositorio.buscar_pet_com_tutor()

      else: 
         print("\n")
         print("opção invalida")
         
   # questão 4
   elif opcao == "4":
      print("\n")
      
      opcao_quatro = input(
         " Digite uma opção: \n" \
         " [1] agendar consulta \n" \
         " [2] adicionar procedimento \n" \
         " [3] remover procedimento \n"\
         " [4] listar procedimentos da consulta \n" \
         " [5] listar consultas por procedimento \n" \
         " [6] total de uma consulta \n" \
         " [7] atualizar status de uma consulta \n" \
         " [8] excluir um consulta \n" \
         " Opção: " )

      if opcao_quatro == "1":
         print("\n")
         id_pet = input("Digite o id de um pet: ")
         id_vet = input("Digite o id de um veterinairo: ")
         data_hora = input("digite a data e hora nesse formato (2026-09-02 09:00):")
         motivo = input("digite o motivo da consulta: ")
         id_procedimento = int(input("Digite o ID do procedimento: "))
         quantidade = int(input("Digite a quantidade: "))

         procedimentos = [(id_procedimento, quantidade)]

         repositorio.agendar_consulta(id_pet,id_vet,data_hora,motivo,procedimentos)

      elif opcao_quatro == "2":
         print("\n")
         repositorio.adicionar_procedimento()

      elif opcao_quatro == "3":
         print("\n")
         repositorio.remover_procedimento()

      elif opcao_quatro == "4":
         print("\n")
         repositorio.listar_procedimentos_da_consulta()

      elif opcao_quatro == "5":
         print("\n")
         repositorio.listar_consultas_por_procedimento()

      elif opcao_quatro == "6":
         print("\n")
         repositorio.total_da_consulta()

      elif opcao_quatro == "7":
         print("\n")
         repositorio.atualizar_status_consulta()

      elif opcao_quatro == "8":
         print("\n")
         repositorio.excluir_consulta()

      else:
         print("\n")
         print("opção invalida")

   # bonus
   elif opcao == "5":
      print("\n")
      repositorio.historico_do_pet()

   print("\n")
   opcao = input(
      "Digite uma opção:\n"
      "[1] Etapa 1 - Testar conexão\n"
      "[2] Etapa 2 - CRUD de tutor\n"
      "[3] Etapa 3 - Relacionamento 1:N tutor → pet\n"
      "[4] Etapa 4 - Relacionamento N:N consulta ↔ procedimento\n"
      "[5] Bônus\n"
      "[sair] para finalizar \n"
      "Opção: "
   )      