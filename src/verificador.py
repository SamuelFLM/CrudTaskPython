import conexao as conexao

cx = conexao.GrupoConexao
comandos = conexao.ArgumentosGrupoSQL


class VerificadorTabelas:

    def valida_criacao_tabela(argumento):
        try:
            if (conexao.validando_tabela_existente(argumento)):
                print('\033[1;31mTABELA JÀ EXISTENTE')
            else:
                cx.executa_query_sql(
                    cx.cria_tabela_sql(argumento))
                print('Tabela Criada com sucesso')

        except ValueError as erro:
            print('\033[1;31mCOMANDO INVALIDO')
        except IndexError as erro:
            print('\033[1;31mCOMANDO INVALIDO')

    def valida_leitura_tabela(argumento):
        try:
            if (conexao.validando_tabela_existente(argumento)):
                comandos.ler_tarefas(argumento)
                input('Aperte para continuar......')
            else:
                print('\033[1;31mTABELA NÃO EXISTENTE')
        except ValueError as erro:
            print('\033[1;31mCOMANDO INVALIDO')
        except IndexError as erro:
            print('\033[1;31mCOMANDO INVALIDO')

    def valida_exclusao_tabela(argumento):
        try:
            if (conexao.validando_tabela_existente(argumento)):
                cx.executa_query_sql(
                    cx.excluir_tabela_sql(argumento))
                print('\033[1;32mTABELA DELETADA COM SUCESSO')
            else:
                print('\033[1;31mTABELA NÃO EXISTENTE')
        except ValueError as erro:
            print('\033[1;31mCOMANDO INVALIDO')
        except IndexError as erro:
            print('\033[1;31mCOMANDO INVALIDO')
