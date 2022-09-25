import pyodbc


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
        [DT_INICIO] DATETIME NOT NULL,
        [DT_FIM] DATETIME NOT NULL
    )
    """
        return sql_criacao_tabela

    def ler_tabela_sql(nome_tabela):
        sql_ler_tabela = f"""
            SELECT * FROM [{nome_tabela}]
        """
        return sql_ler_tabela

    def excluir_tabela_sql(nome_tabela):
        sql_excluir_tabela = f"""
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
