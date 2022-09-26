import conexao
from datetime import date, datetime


class Estrutura:
    cx = conexao
    comandos = conexao.ArgumentosGrupoSQL
    # OK CRIA TABELA
    # cx.GrupoConexao.executa_query_sql(
    #     cx.GrupoConexao.cria_tabela_sql('faculdade'))

    # OK DELETA TABELA
    # cx.GrupoConexao.executa_query_sql(
    #     cx.GrupoConexao.excluir_tabela_sql('faculdade'))

    # OK INSERI INFORMAÇÃO TABELA
    # data = datetime.now()
    # cx.GrupoConexao.executa_query_sql(comandos.adicionar_tarefa(
    #     'faculdade', 'tedio', 'A', 'P', data.__format__('%d/%m/%Y %H:%M:%S'), data.__format__('%d/%m/%Y %H:%M:%S')))

    # OK LER INFORMAÇÃO
    # comandos.ler_tarefas('faculdade')

    # OK COMPLETAR TAREFAS
    # cx.GrupoConexao.executa_query_sql(comandos.complete_tarefa('faculdade', 1))

    # OK ALTERAR TAREFAS
    # cx.GrupoConexao.executa_query_sql(comandos.alterar_tarefa(
    #     'faculdade', 'descricao', 'Descricao bolada hehe', 1))

    # OK DELETAR TAREFAS
    # cx.GrupoConexao.executa_query_sql(comandos.deleta_tarefa('faculdade', 1))
