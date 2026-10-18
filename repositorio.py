import db
import pyodbc

# Etapa 2 — CRUD de tutor
def validar_cpf(cpf):
   cpf = str(cpf).replace(".", "").replace("-", "")

   if len(cpf) != 11 or not cpf.isdigit():
      raise ValueError("CPF inválido.")

   conn = db.conectar()

   try:
      cursor = conn.cursor()

      cursor.execute(
         "SELECT id_tutor FROM dbo.tutor WHERE cpf = ?",
         cpf
      )

      if cursor.fetchone():
         raise ValueError("CPF já cadastrado.")

   finally:
      cursor.close()
      conn.close()

   return cpf
      
def criar_tutor():
   nome = input("Digite o nome do tutor: ")
   cpf = input("Digite o CPF do tutor: ")

   try:
      cpf = validar_cpf(cpf)
   except ValueError as erro:
      print(f"\nErro: {erro}\n")
      return None

   email = input("Digite o email do tutor: ")
   telefone = input("Digite o telefone do tutor: ")

   conn = db.conectar()

   try:
      cursor = conn.cursor()

      query = """ 
            INSERT INTO dbo.tutor (nome, cpf, email, telefone) 
            OUTPUT INSERTED.id_tutor
            VALUES (?, ?, ?, ?)
        """

      cursor.execute(query, nome, cpf, email, telefone)

      id_tutor = cursor.fetchone()[0]

      conn.commit()

      return id_tutor

   except Exception:
      conn.rollback()
      raise

   finally:
      cursor.close()
      conn.close()
   
def buscar_tutor():
   id_tutor = input("Digite o ID do tutor: ")

   conn = db.conectar()

   try:
      cursor = conn.cursor()

      query = """
            SELECT id_tutor, nome, cpf, email, telefone
            FROM dbo.tutor
            WHERE id_tutor = ?
      """

      cursor.execute(query, id_tutor)
      tutor = cursor.fetchone()

      if tutor:
         return tutor
      else:
         print("Tutor não encontrado.")
         return None

   finally:
      cursor.close()
      conn.close()

def listar_tutores(filtro_nome=None):
   conn = db.conectar()

   try:
      cursor = conn.cursor()

      if filtro_nome:
         query = """
            SELECT id_tutor, nome, cpf, email, telefone
            FROM dbo.tutor
            WHERE nome LIKE ?
            ORDER BY nome
         """

         cursor.execute(query, f"%{filtro_nome}%")

      else:
         query = """
            SELECT id_tutor, nome, cpf, email, telefone
            FROM dbo.tutor
            ORDER BY nome
         """

         cursor.execute(query)

      tutores = cursor.fetchall()
      return tutores

   finally:
      cursor.close()
      conn.close()

def atualizar_tutor(id_tutor, **campos):
   campos_permitidos = ["nome", "email", "telefone"]

   if not campos:
      print("Nenhum campo informado para atualização.")
      return

   for campo in campos:
      if campo not in campos_permitidos:
         print(f"Campo não permitido: {campo}")
         return

   conn = db.conectar()

   try:
      cursor = conn.cursor()

      atualizacoes = ", ".join(
         f"{campo} = ?" for campo in campos
      )

      query = f"""
         UPDATE dbo.tutor
         SET {atualizacoes}
         WHERE id_tutor = ?
      """

      valores = list(campos.values())
      valores.append(id_tutor)

      cursor.execute(query, valores)

      if cursor.rowcount == 0:
         print("Tutor não encontrado.")
         conn.rollback()
         return False

      conn.commit()
      print("Tutor atualizado com sucesso!")
      return True

   except Exception:
      conn.rollback()
      raise

   finally:
      cursor.close()
      conn.close()
     
def excluir_tutor():

   id_tutor = input("Digite o ID do tutor que deseja excluir: ")

   conn = db.conectar()

   try:
      cursor = conn.cursor()

      query = """
         DELETE FROM dbo.tutor
         WHERE id_tutor = ?
      """

      cursor.execute(query, id_tutor)

      if cursor.rowcount == 0:
         conn.rollback()
         print("Tutor não encontrado.")
         return False

      conn.commit()
      print("Tutor excluído com sucesso!")
      return True

   except pyodbc.IntegrityError:
      conn.rollback()
      print("Não é possível excluir este tutor, pois ele possui pets cadastrados.")
      return False

   finally:
      conn.close()

# Etapa 3 — Relacionamento 1:N tutor → pet
def criar_pet():
   id_tutor = input("Digite o ID do tutor: ")
   nome = input("Digite o nome do pet: ")
   especie = input("Digite a espécie do pet: ")
   raca = input("Digite a raça do pet: ")
   data_nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
   peso_kg = input("Digite o peso do pet em kg: ")

   conn = db.conectar()

   try:
      cursor = conn.cursor()

      query = """
         INSERT INTO dbo.pet
            (id_tutor, nome, especie, raca, data_nascimento, peso_kg)
         OUTPUT INSERTED.id_pet
         VALUES (?, ?, ?, ?, ?, ?)
      """

      cursor.execute(
         query,
         id_tutor,
         nome,
         especie,
         raca,
         data_nascimento,
         peso_kg
      )

      id_pet = cursor.fetchone()[0]
      conn.commit()

      print(f"Pet cadastrado com sucesso! ID: {id_pet}")
      return id_pet

   except pyodbc.IntegrityError:
      conn.rollback()
      print("Não foi possível cadastrar. Verifique o tutor e os dados informados.")
      return None

   except pyodbc.Error as erro:
      conn.rollback()
      print(f"Erro ao cadastrar pet: {erro}")
      return None

   finally:
      cursor.close()
      conn.close()

def atualizar_peso_pet():

   id_pet = input("Digite o ID do pet: ")
   peso = input("Digite o novo peso: ")

   conn = db.conectar()

   try:
      cursor = conn.cursor()

      query = """
         UPDATE dbo.pet
         SET peso_kg = ?
         WHERE id_pet = ?
      """

      cursor.execute(query, peso, id_pet)

      if cursor.rowcount == 0:
         conn.rollback()
         print("Pet não encontrado.")
         return 

      conn.commit()
      print("Peso atualizado com sucesso!")
      return True

   except pyodbc.Error as erro:
      conn.rollback()
      print(f"Erro ao atualizar peso: {erro}")
      return False

   finally:
      cursor.close()
      conn.close()

def transferir_pet():
   id_pet = input("Digite o ID do pet: ")
   novo_id_tutor = input("Digite o ID do novo tutor: ")

   conn = db.conectar()

   try:
      cursor = conn.cursor()

      query = """
         UPDATE dbo.pet
         SET id_tutor = ?
         WHERE id_pet = ?
      """

      cursor.execute(query, novo_id_tutor, id_pet)

      if cursor.rowcount == 0:
         conn.rollback()
         print("Pet não encontrado.")
         return 

      conn.commit()
      print("Pet transferido com sucesso!")
      return 

   except pyodbc.IntegrityError:
      conn.rollback()
      print("Não foi possível transferir. Verifique se o novo tutor existe.")
      return 

   except pyodbc.Error as erro:
      conn.rollback()
      print(f"Erro ao transferir pet: {erro}")
      return False

   finally:
      cursor.close()
      conn.close()

def excluir_pet():
   id_pet = input("Digite o ID do pet que deseja excluir: ")

   conn = db.conectar()

   try:
      cursor = conn.cursor()

      query = """
         DELETE FROM dbo.pet
         WHERE id_pet = ?
      """

      cursor.execute(query, id_pet)

      if cursor.rowcount == 0:
         conn.rollback()
         print("Pet não encontrado.")
         return 

      conn.commit()
      print("Pet excluído com sucesso!")
      return 

   except pyodbc.IntegrityError:
      conn.rollback()
      print("Não é possível excluir este pet, pois ele possui consultas cadastradas.")
      return False

   except pyodbc.Error as erro:
      conn.rollback()
      print(f"Erro ao excluir pet: {erro}")
      return False

   finally:
      cursor.close()
      conn.close()

def listar_pets_do_tutor():
   id_tutor = input("Digite o ID do tutor: ")

   conn = db.conectar()

   try:
      cursor = conn.cursor()

      query = """
         SELECT id_pet, nome, especie, raca , peso_kg
         FROM dbo.pet
         WHERE id_tutor = ?
         ORDER BY nome
      """

      cursor.execute(query, id_tutor)
      pets = cursor.fetchall()

      if not pets:
         print("\nNenhum pet encontrado para esse tutor.")
         return []

      for pet in pets:
         print(
            f"ID: {pet.id_pet} | "
            f"Nome: {pet.nome} | "
            f"Espécie: {pet.especie} | "
            f"raca: {pet.raca} | "
            f"Peso: {pet.peso_kg}"
         )

      return pets

   except pyodbc.Error as erro:
      print(f"Erro ao listar pets: {erro}")
      return []

   finally:
      cursor.close()
      conn.close()

def buscar_pet_com_tutor():
   id_pet = input("Digite o ID do pet: ")

   conn = db.conectar()

   try:
      cursor = conn.cursor()

      query = """
         SELECT
            p.id_pet,
            p.nome AS nome_pet,
            p.especie,
            p.raca,
            p.peso_kg,
            t.id_tutor,
            t.nome AS nome_tutor
         FROM dbo.pet AS p
         INNER JOIN dbo.tutor AS t
         ON p.id_tutor = t.id_tutor
         WHERE p.id_pet = ?
      """

      cursor.execute(query, id_pet)
      pet = cursor.fetchone()

      if pet:
         print(
            f"ID: {pet.id_pet} | "
            f"Nome: {pet.nome_pet} | "
            f"Espécie: {pet.especie} | "
            f"raca: {pet.raca} | "
            f"Peso: {pet.peso_kg}"
         )
         print(f"ID do tutor: {pet.id_tutor} | Nome do tutor: {pet.nome_tutor}")

         return pet

      print("\nPet não encontrado.")
      return None

   except pyodbc.Error as erro:
      print(f"\nErro ao buscar pet: {erro}")
      return None

   finally:
      cursor.close()
      conn.close()

# Etapa 4 — Relacionamento N:N consulta ↔ procedimento
def agendar_consulta(id_pet, id_vet, data_hora, motivo, procedimentos):
   conn = db.conectar()

   try:
      cursor = conn.cursor()

      query = """
         INSERT INTO dbo.consulta
            (id_pet, id_veterinario, data_hora, motivo, status)
         OUTPUT INSERTED.id_consulta
         VALUES (?, ?, ?, ?, 'AGENDADA')
      """

      cursor.execute(query, id_pet, id_vet, data_hora, motivo)
      id_consulta = cursor.fetchone()[0]

      for id_procedimento, quantidade in procedimentos:
         cursor.execute("""
            SELECT preco_base
            FROM dbo.procedimento
            WHERE id_procedimento = ?
         """, id_procedimento)

         procedimento = cursor.fetchone()

         if not procedimento:
            raise ValueError(
               f"Procedimento {id_procedimento} não encontrado."
            )

         preco = procedimento.preco_base

         cursor.execute("""
            INSERT INTO dbo.consulta_procedimento
               (id_consulta, id_procedimento, quantidade, valor_cobrado)
            VALUES (?, ?, ?, ?)
         """, id_consulta, id_procedimento, quantidade, preco)

      conn.commit()
      print(f"Consulta agendada com sucesso! ID: {id_consulta}")
      return id_consulta

   except (ValueError, pyodbc.Error) as erro:
      conn.rollback()
      print(f"Erro ao agendar consulta: {erro}")
      return None

   finally:
      cursor.close()
      conn.close()

def adicionar_procedimento():
   id_consulta = input("digite o id da consulta: ")
   id_procedimento = input("digite o id da procedimento: ")
   quantidade = int(input("digite a quantidade desse procedimento: "))
   conn = db.conectar()

   try:
      cursor = conn.cursor()

      # Verifica se a consulta existe e não está cancelada
      cursor.execute("""
         SELECT status
         FROM dbo.consulta
         WHERE id_consulta = ?
      """, id_consulta)

      consulta = cursor.fetchone()

      if not consulta:
         raise ValueError("Consulta não encontrada.")

      if consulta.status == "CANCELADA":
         raise ValueError("Não é possível alterar uma consulta cancelada.")

      if quantidade <= 0:
         raise ValueError("A quantidade deve ser maior que zero.")

      # Busca o preço do procedimento
      cursor.execute("""
         SELECT preco_base
         FROM dbo.procedimento
         WHERE id_procedimento = ?
      """, id_procedimento)

      procedimento = cursor.fetchone()

      if not procedimento:
         raise ValueError("Procedimento não encontrado.")

      # Insere na tabela associativa
      cursor.execute("""
         INSERT INTO dbo.consulta_procedimento
            (id_consulta, id_procedimento, quantidade, valor_cobrado)
         VALUES (?, ?, ?, ?)
      """, id_consulta, id_procedimento, quantidade,
           procedimento.preco_base)

      conn.commit()
      print("Procedimento adicionado com sucesso!")
      return

   except (ValueError, pyodbc.Error) as erro:
      conn.rollback()
      print(f"Erro ao adicionar procedimento: {erro}")
      return

   finally:
      cursor.close()
      conn.close()

def remover_procedimento():
   id_consulta = input("Digite o ID da consulta: ")
   id_procedimento = input("Digite o ID do procedimento: ")
   conn = db.conectar()

   try:
      cursor = conn.cursor()

      # Verifica se a consulta existe e não está cancelada
      cursor.execute("""
         SELECT status
         FROM dbo.consulta
         WHERE id_consulta = ?
      """, id_consulta)

      consulta = cursor.fetchone()

      if not consulta:
         raise ValueError("Consulta não encontrada.")

      if consulta.status == "CANCELADA":
         raise ValueError("Não é possível alterar uma consulta cancelada.")

      # Remove o procedimento da tabela associativa
      cursor.execute("""
         DELETE FROM dbo.consulta_procedimento
         WHERE id_consulta = ?
           AND id_procedimento = ?
      """, id_consulta, id_procedimento)

      if cursor.rowcount == 0:
         raise ValueError(
            "Esse procedimento não está vinculado a essa consulta."
         )

      conn.commit()
      print("Procedimento removido com sucesso!")
      return

   except (ValueError, pyodbc.Error) as erro:
      conn.rollback()
      print(f"Erro ao remover procedimento: {erro}")
      return

   finally:
      cursor.close()
      conn.close()

def listar_procedimentos_da_consulta():
   id_consulta = input("Digite o ID da consulta: ")
   conn = db.conectar()

   try:
      cursor = conn.cursor()

      cursor.execute("""
         SELECT
            p.id_procedimento,
            p.descricao,
            cp.quantidade,
            cp.valor_cobrado
         FROM dbo.consulta_procedimento AS cp
         INNER JOIN dbo.procedimento AS p
            ON cp.id_procedimento = p.id_procedimento
         WHERE cp.id_consulta = ?
      """, id_consulta)

      procedimentos = cursor.fetchall()

      if not procedimentos:
         print("Nenhum procedimento encontrado para essa consulta.")
         return

      print(f"\nProcedimentos da consulta {id_consulta}:")

      for procedimento in procedimentos:
         subtotal = procedimento.quantidade * procedimento.valor_cobrado

         print(f"""
            ID: {procedimento.id_procedimento}
            Descrição: {procedimento.descricao}
            Quantidade: {procedimento.quantidade}
            Valor unitário: R$ {procedimento.valor_cobrado:.2f}
            Subtotal: R$ {subtotal:.2f}
         """)

   except pyodbc.Error as erro:
      print(f"Erro ao listar procedimentos: {erro}")

   finally:
      cursor.close()
      conn.close()

def listar_consultas_por_procedimento():
   id_procedimento = input("Digite o ID do procedimento: ")
   conn = db.conectar()

   try:
      cursor = conn.cursor()

      cursor.execute("""
         SELECT
            c.id_consulta,
            c.id_pet,
            c.id_veterinario,
            c.data_hora,
            c.status,
            cp.quantidade,
            cp.valor_cobrado
         FROM dbo.consulta_procedimento AS cp
         INNER JOIN dbo.consulta AS c
            ON cp.id_consulta = c.id_consulta
         WHERE cp.id_procedimento = ?
      """, id_procedimento)

      consultas = cursor.fetchall()

      if not consultas:
         print("Nenhuma consulta encontrada para esse procedimento.")
         return

      print(f"\nConsultas com o procedimento {id_procedimento}:")

      for consulta in consultas:
         print(f"""
         ID da consulta: {consulta.id_consulta}
         ID do pet: {consulta.id_pet}
         ID do veterinário: {consulta.id_veterinario}
         Data e hora: {consulta.data_hora}
         Status: {consulta.status}
         Quantidade: {consulta.quantidade}
         Valor unitário: R$ {consulta.valor_cobrado:.2f}
         """)

   except pyodbc.Error as erro:
      print(f"Erro ao listar consultas: {erro}")

   finally:
      cursor.close()
      conn.close()

def total_da_consulta():
   id_consulta = input("Digite o ID da consulta: ")
   conn = db.conectar()

   try:
      cursor = conn.cursor()

      # Verifica se a consulta existe
      cursor.execute("""
         SELECT id_consulta
         FROM dbo.consulta
         WHERE id_consulta = ?
      """, id_consulta)

      if cursor.fetchone() is None:
         print ("\nConsulta não encontrada.\n")
         return


      # Calcula o total dos procedimentos
      cursor.execute("""
         SELECT (
            SUM(quantidade * valor_cobrado)
         ) AS total
         FROM dbo.consulta_procedimento
         WHERE id_consulta = ?
      """, id_consulta)

      resultado = cursor.fetchone()

      print(f"Total da consulta: R$ {resultado.total:.2f}")

   except pyodbc.Error as erro:
      print(f"Erro ao calcular total da consulta: {erro}")

   finally:
      cursor.close()
      conn.close()

def atualizar_status_consulta():
   id_consulta = input("Digite o ID da consulta: ")
   novo_status = input(
      "Digite o novo status (AGENDADA, REALIZADA, CANCELADA): "
   ).strip().upper()

   conn = db.conectar()

   try:
      cursor = conn.cursor()

      status_validos = ("AGENDADA", "REALIZADA", "CANCELADA")

      if novo_status not in status_validos:
         raise ValueError("Status inválido.")

      cursor.execute("""
         UPDATE dbo.consulta
         SET status = ?
         WHERE id_consulta = ?
      """, novo_status, id_consulta)

      if cursor.rowcount == 0:
         raise ValueError("Consulta não encontrada.")

      conn.commit()
      print("Status da consulta atualizado com sucesso!")

   except (ValueError, pyodbc.Error) as erro:
      conn.rollback()
      print(f"Erro ao atualizar status: {erro}")

   finally:
      cursor.close()
      conn.close()

def excluir_consulta():
   id_consulta = input("Digite o ID da consulta que deseja excluir: ")
   conn = db.conectar()

   try:
      cursor = conn.cursor()

      cursor.execute("""
         DELETE FROM dbo.consulta
         WHERE id_consulta = ?
      """, id_consulta)

      if cursor.rowcount == 0:
         raise ValueError("Consulta não encontrada.")

      conn.commit()
      print("Consulta excluída com sucesso!")

   except (ValueError, pyodbc.Error) as erro:
      conn.rollback()
      print(f"Erro ao excluir consulta: {erro}")

   finally:
      cursor.close()
      conn.close()


# Bonus


def historico_do_pet():
   id_pet = input("Digite o ID do pet: ")

   conn = db.conectar()
   cursor = None

   try:
      cursor = conn.cursor()

      cursor.execute("""
         SELECT h.*
         FROM dbo.vw_resumo_consulta h
         JOIN dbo.pet p ON p.nome = h.pet
         WHERE p.id_pet = ?
      """, id_pet)

      historico = cursor.fetchall()

      if not historico:
         print("Nenhum histórico encontrado para esse pet.")
         return

      colunas = [coluna[0] for coluna in cursor.description]

      print("\nHistórico de consultas do pet:")

      for registro in historico:
         print("\n------------------------------")

         for coluna, valor in zip(colunas, registro):
            print(f"{coluna}: {valor}")

   except pyodbc.Error as erro:
      print(f"Erro ao consultar histórico do pet: {erro}")

   finally:
      cursor.close()
      conn.close()

