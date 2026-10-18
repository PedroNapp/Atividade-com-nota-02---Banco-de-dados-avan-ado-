Projeto desenvolvido em Python para a atividade **Desafio Técnico — Conexão Python + SQL Server com pyodbc**.

O objetivo é implementar uma camada de acesso a dados para o banco de dados PetVida, permitindo realizar operações de cadastro, consulta, atualização e exclusão de informações relacionadas a tutores, pets, consultas veterinárias e procedimentos.

## 1. Tecnologias utilizadas

- **Python:** implementação da aplicação.
- **Microsoft SQL Server:** sistema gerenciador do banco de dados.
- **pyodbc:** biblioteca utilizada para conectar o Python ao SQL Server.

## 2. Estrutura do projeto

```text
PetVida/
├── config.py
├── db.py
├── repositorio.py
├── main.py
└── README.md
```

| Arquivo | Responsabilidade |
|---|---|
| `config.py` | Armazena as variáveis de configuração da conexão. |
| `db.py` | Monta a string de conexão, estabelece a conexão e testa o acesso ao banco. |
| `repositorio.py` | Implementa as operações de acesso e manipulação dos dados. |
| `main.py` | Apresenta o menu de terminal e permite acessar as funcionalidades do sistema. |

## 3. Requisitos para execução

Antes de executar o projeto, verifique se o ambiente possui:

- Python instalado.
- Microsoft SQL Server instalado e em execução.
- Banco de dados `PetVida` criado conforme o script fornecido na atividade (com a parte opicional) .
- Permissões de acesso ao banco de dados.
- Biblioteca Python `pyodbc` instalada.

## 4. Configuração das variáveis

No arquivo `config.py`, configure o nome da instância do SQL Server utilizada no ambiente.

Exemplo:

```python
usuario = ""
senha = ""

server = "PEDROLIOS\SQLEXPRESS"
```

A variável `server` deve corresponder ao servidor utilizado no computador. Caso servidor do SQL Server esteja instalado em outra instância, esse valor deverá ser atualizado.

As variáveis `usuario` e `senha` devem permanecer vazias no arquivo, pois as credenciais são solicitadas durante a execução do programa. Elas são utilizadas para reaproveitar os dados informados durante o processo de conexão.

### Configuração da autenticação

A instância deve aceitar o método de autenticação utilizado pela aplicação.

Neste projeto, foi utilizada a autenticação do SQL Server com o login `petvida_app`. Caso esse login ainda não exista, deve ser criado conforme o script de configuração disponibilizado na atividade, com as permissões necessárias para acessar o banco `PetVida`.

Usuário SQL Server: petvida_app  
Senha SQL Server: PetVida@2026!

## 5. Instalação da dependência

Abra o terminal na pasta do projeto e execute:

```bash
pip install pyodbc
```

## 6. Como executar o projeto

Na pasta principal do projeto, execute:

```bash
python main.py
```

O programa solicitará as credenciais do SQL Server e tentará estabelecer a conexão com o banco de dados.

Após uma conexão bem-sucedida, serão exibidas as informações do servidor, do banco e da versão do SQL Server. Em seguida, o menu principal permitirá acessar as operações implementadas no repositório.

Se a conexão falhar, confira o nome da instância, as credenciais, o método de autenticação e as permissões do login.
