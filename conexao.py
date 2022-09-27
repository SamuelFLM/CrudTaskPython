import pyodbc
import pandas as pd


def dados_conexao(DriveDoBancoDeDados, host, database, user_server, pwd):
    dados_conexao = (
        f"Driver={DriveDoBancoDeDados};"
        f"Server={host};"
        f"Database={database};"
        f"UID={user_server};"
        f"PWD={pwd}"
    )
    return dados_conexao
# Informações necessarias para conectar no banco de dados.


conexao_banco_de_dados = pyodbc.connect(dados_conexao('SQL SERVER Native Client 11.0',
                                                      host='samu', database='TO-DO', user_server='sa', pwd='sa270212'))
# Conexão com banco de dados

cursor = conexao_banco_de_dados.cursor()
# Cursor responsavel por executar query


class GrupoConexao:

    def cria_tabela_sql(nome_tabela):
        sql_criacao_tabela = f"""
        CREATE TABLE [{nome_tabela}](
        [ID] INT IDENTITY NOT NULL,
        [DESCRICAO] NVARCHAR(30) NOT NULL,
        [PRIORIDADE] CHAR(1) NOT NULL,
        [STATUS] CHAR(2) NOT NULL,
        [DT_INICIO] NVARCHAR(30) NOT NULL,
        [DT_FIM] NVARCHAR(30)
    )
    """
        return sql_criacao_tabela

    def ler_tabela_sql(nome_tabela):
        tabela = pd.read_sql(
            f'SELECT * FROM [{nome_tabela}]', conexao_banco_de_dados)
        return print(tabela)

    def excluir_tabela_sql(nome_tabela):
        sql_excluir_tabela = f"""
            USE [TO-DO]
            DROP TABLE [{nome_tabela}]
        """
        return sql_excluir_tabela

    def executa_query_sql(nome_metodo):
        cursor.execute(nome_metodo)
        cursor.commit()


class ArgumentosGrupoSQL:
    # <id> <descricao> <prioridade> <status> <dt_inicio> <dt_fim>
    def adicionar_tarefa(nome_tabela, descricao, prioridade, status, dt_inicio, dt_fim):
        sql_adiciona_tarefa = f"""
        INSERT INTO [{nome_tabela}] VALUES ('{descricao}', '{prioridade}', '{status}', '{dt_inicio}', '{dt_fim}')
        """
        return sql_adiciona_tarefa

    def complete_tarefa(nome_tabela, id_tarefa):
        sql_complete_tarefa = f"""
            USE [TO-DO]
            UPDATE [{nome_tabela}]
                SET [STATUS] = 'OK'
                WHERE [ID] = {id_tarefa}
        """
        return sql_complete_tarefa

    def deleta_tarefa(nome_tabela, id_tarefa):
        sql_deleta_tarefa = f"""
        DELETE [{nome_tabela}] WHERE [ID] = {id_tarefa}
        """
        return sql_deleta_tarefa

    def ler_tarefas(nome_tabela):
        tabela = pd.read_sql(
            f'SELECT * FROM [{nome_tabela}]', conexao_banco_de_dados)
        return print(tabela)

    def alterar_tarefa(nome_tabela, coluna, descricao, id_tarefa):
        sql_altera_tarefa = f"""
        USE [TO-DO]
        UPDATE [{nome_tabela}]
        SET [{coluna}] = '{descricao}'
        WHERE [ID] = {id_tarefa}
        """
        return sql_altera_tarefa


def validando_tabela_existente(nome_tabela):
    sql_verificando_existencia_tabela = f"""
    SELECT TABLE_NAME FROM information_schema.tables WHERE TABLE_NAME = '{nome_tabela}';
    """
    cursor.execute(sql_verificando_existencia_tabela)
    rows = cursor.fetchall()
    return rows
