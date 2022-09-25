import conexao
from datetime import datetime


class Estrutura:
    cx = conexao
    comandos = conexao.ArgumentosGrupoSQL
    # cx.GrupoConexao.executa_query_sql(
    #     cx.GrupoConexao.cria_tabela_sql('faculdade'))

    cx.GrupoConexao.executa_query_sql(comandos.adicionar_tarefa(
        'faculdade', 'tedio', 'A', 'P', datetime.now(), datetime.now()))
