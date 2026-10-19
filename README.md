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

<img width="1202" height="346" alt="image" src="https://github.com/user-attachments/assets/a8bd606b-e39c-4fe0-8f13-a30e9183ae81" />
print de uma conceção bem sucedida 

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

Prints do validador:
-- Questão 1 --
![Print de uma conexão bem-sucedida](https://github.com/user-attachments/assets/b11bf36e-9ce9-4032-96ff-4cea8971a721")

-- Quetão 2 --

menu de seleção:
![Print do menu de seleção](https://github.com/user-attachments/assets/f0fc2493-23e9-4abb-847f-7cec7272d056)

criar tutor () funcionamento e verificações de erro:
![Print do criar tutor sucesso](https://github.com/user-attachments/assets/b52fc2d7-89cf-4a2d-ab65-09b5f170370a)
![Print do criar tutor erro](https://github.com/user-attachments/assets/58f834d8-98a4-4111-9ac6-8db93124dcaf)

buscar tutor por ID :
tinha feito update antes por isso ta diferente da estrutura da atividade 
![Print do buscar tutor sucesso](https://github.com/user-attachments/assets/b1e70359-31e8-4cb9-af43-bde33fb7ee26)
![Print do buscar tutor erro](https://github.com/user-attachments/assets/0131fe4c-7d02-40f6-88d1-5c626fe05e81)



listar_tutores(filtro_nome):
<img width="610" height="282" alt="image" src="https://github.com/user-attachments/assets/91bca57e-ad86-4a00-be1b-23776086f41c" />
<img width="566" height="277" alt="image" src="https://github.com/user-attachments/assets/673bc25c-82d0-4390-8de0-2b3d27bd3499" />
<img width="855" height="360" alt="image" src="https://github.com/user-attachments/assets/e241d0b5-76f7-44a8-b1ab-4f302d4bad60" />



atualizar_tutor(id, **campos):
estrutura interna:
<img width="762" height="232" alt="image" src="https://github.com/user-attachments/assets/3e82e988-27e8-480f-8ec8-bd85d7efe07c" />
<img width="1096" height="217" alt="image" src="https://github.com/user-attachments/assets/c07f2e33-67bd-4cd4-9202-f30b691b3e15" />



teste funcionando:
<img width="472" height="357" alt="image" src="https://github.com/user-attachments/assets/8d47e867-ea52-432d-8816-cc86af09c014" />
<img width="587" height="247" alt="image" src="https://github.com/user-attachments/assets/4d24c8fa-ca5f-45d9-b1d0-7c7f27388dc4" />



id_invalido:
<img width="361" height="355" alt="image" src="https://github.com/user-attachments/assets/51dd40d1-2fda-44ca-ad2c-481bec766d3d" />



erro com campo fora da lista:
<img width="457" height="340" alt="image" src="https://github.com/user-attachments/assets/b8fe8b9a-853a-49b8-a676-d5e771418c2f" />



Delete: excluir_tutor():
<img width="430" height="277" alt="image" src="https://github.com/user-attachments/assets/e8d9c5eb-734c-4b26-9d22-a858067e4228" />
<img width="667" height="270" alt="image" src="https://github.com/user-attachments/assets/4dc00f53-3d2d-45c2-a853-3bb98975521d" />



Etapa 3 — Relacionamento 1:N tutor → pet 
criar_pet():
<img width="500" height="452" alt="image" src="https://github.com/user-attachments/assets/88968d77-4145-46f0-b470-d7f519b15bea" />
<img width="657" height="187" alt="image" src="https://github.com/user-attachments/assets/59ee8e18-c888-47d1-8bbc-fdc7a4cec937" />



atualizar pesso:
<img width="362" height="342" alt="image" src="https://github.com/user-attachments/assets/61362bf3-8095-444a-b702-1a08bb078bc9" />
<img width="287" height="311" alt="image" src="https://github.com/user-attachments/assets/183a401a-1905-4d34-a27d-04c879e6dc16" />



transferir_pet()
<img width="630" height="236" alt="image" src="https://github.com/user-attachments/assets/783953a9-c675-49eb-83b3-35fc68e06cfb" />
<img width="322" height="236" alt="image" src="https://github.com/user-attachments/assets/73b42cfe-33e3-4210-9ea3-c4b32950e257" />



excluir_pet():
<img width="680" height="297" alt="image" src="https://github.com/user-attachments/assets/f18d936f-0c18-4a23-9ff9-2689457c9960" />
<img width="407" height="296" alt="image" src="https://github.com/user-attachments/assets/817eda3e-a1f1-4602-a74f-824cd8cefe41" />



listar_pets_do_tutor():
<img width="627" height="290" alt="image" src="https://github.com/user-attachments/assets/1e5fad31-c415-445a-9acb-60c9e1bba69d" />
<img width="707" height="101" alt="image" src="https://github.com/user-attachments/assets/b6707cc7-587d-4b4b-a843-c35606d8fff1" />
<img width="397" height="237" alt="image" src="https://github.com/user-attachments/assets/ec0ca3b7-b4ff-47bd-8aac-e2e8992afebe" />



buscar_pet_com_tutor():
<img width="727" height="187" alt="image" src="https://github.com/user-attachments/assets/b635d2ab-19ab-4c9f-9636-d5db66c41f28" />
<img width="357" height="252" alt="image" src="https://github.com/user-attachments/assets/1ec445a3-bc46-45e7-b0d1-98c35f1094ba" />



Etapa 4 — Relacionamento N:N consulta ↔ procedimento 
agendar_consulta(id_pet, id_vet, data_hora, motivo, procedimentos)
<img width="687" height="442" alt="image" src="https://github.com/user-attachments/assets/2be2c8e3-9f9b-403f-88a7-ff7066d23c2b" />
<img width="1485" height="450" alt="image" src="https://github.com/user-attachments/assets/12be30c3-da7c-498c-8ea9-ee154081ee12" />



adicionar_procedimento()
<img width="456" height="387" alt="image" src="https://github.com/user-attachments/assets/27cdeab7-7f12-4504-a14d-e7684b854980" />
procedimento repetido:
<img width="1480" height="425" alt="image" src="https://github.com/user-attachments/assets/281b348a-e052-4286-8004-bdc5cb22cefe" />



remover_procedimento()
<img width="501" height="395" alt="image" src="https://github.com/user-attachments/assets/6198aeb0-0061-4d56-8479-6a052090abcf" />
<img width="822" height="367" alt="image" src="https://github.com/user-attachments/assets/e1c2d0bb-4329-4d6f-9a00-5a3d9df0e058" />



listar_procedimentos_da_consulta()
<img width="482" height="440" alt="image" src="https://github.com/user-attachments/assets/fb47527a-be31-4d4b-a4d0-8ac90ec2b15f" />
<img width="530" height="391" alt="image" src="https://github.com/user-attachments/assets/68c9c244-e248-44eb-a86c-cb019b4cf3c5" />



listar_consultas_por_procedimento()
<img width="432" height="432" alt="image" src="https://github.com/user-attachments/assets/1d7378fb-294d-4d1e-9fed-739af0a67d96" />
<img width="371" height="412" alt="image" src="https://github.com/user-attachments/assets/2328b83a-35b3-43b3-bbc5-4823a2f1161f" />
<img width="512" height="137" alt="image" src="https://github.com/user-attachments/assets/6642e61b-3c3b-472c-9124-01d91b0f2357" />



total_da_consulta()
<img width="291" height="136" alt="image" src="https://github.com/user-attachments/assets/12b2e180-12ef-4828-9774-462b8ccf267c" />
<img width="320" height="152" alt="image" src="https://github.com/user-attachments/assets/ae22a518-e7a5-4ad8-a83e-8d3cd49d8e8d" />



atualizar_status_consulta() 
<img width="637" height="315" alt="image" src="https://github.com/user-attachments/assets/cb751a7d-9fc2-4a87-9221-0ba0057e1406" />
<img width="635" height="256" alt="image" src="https://github.com/user-attachments/assets/80d10aeb-df78-4b57-ac8a-230d62bfc5e4" />



excluir_consulta():
<img width="457" height="330" alt="image" src="https://github.com/user-attachments/assets/8ec68661-0683-4dca-b943-621d4d6ed495" />
<img width="496" height="235" alt="image" src="https://github.com/user-attachments/assets/476f397f-4c67-4805-a60f-bdad29c3de33" />



Bonus:
<img width="510" height="460" alt="image" src="https://github.com/user-attachments/assets/deb25026-169d-4e90-8da8-7e17304260b5" />
