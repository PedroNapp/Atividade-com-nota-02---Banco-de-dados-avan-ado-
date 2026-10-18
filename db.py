import pyodbc
import config

# fiz a tentativa 8. (OPCIONAL) Login SQL dedicado para a aplicação Python
def montar_connection_string():

   conn_str = (
      r"Driver={SQL Server};"
      f"Server={config.server};"
      r"Database=PetVida;"
      f"UID={config.usuario};"
      f"PWD={config.senha};"
   )

   return conn_str


def conectar():
   return pyodbc.connect(
      montar_connection_string(),
      autocommit=False
   )


def testar_conexao():
   conn = conectar()

   try:
      cursor = conn.cursor()

      cursor.execute("""
         SELECT
            @@SERVERNAME AS servidor,
            DB_NAME() AS banco,
            @@VERSION AS versao
      """)

      resultado = cursor.fetchone()

      return {
         "servidor": resultado.servidor,
         "banco": resultado.banco,
         "versao": resultado.versao
      }

   finally:
      cursor.close()
      conn.close()