import conexao
from datetime import datetime
import os
import time


class EstruturaMain:
    cx = conexao
    comandos = conexao.ArgumentosGrupoSQL

    def main():
        argumentoUsuario = ArgumentosUsuario
        argumentoUsuario.argumento_main()
        verificador_grupo = ['CREATE', 'READ', 'DELETE']
        while True:
            time.sleep(1)
            os.system('cls')
            try:
                argumento_usuario = input('\033[1;32mDigite: ').split(' ')
                if (argumento_usuario[1].upper() in verificador_grupo):

                    if (argumento_usuario[1] == verificador_grupo[0]):
                        if (conexao.validando_tabela_existente(argumento_usuario[2])):
                            print('\033[1;31mTABELA JÀ EXISTENTE')
                        else:
                            print('Tabela Criada com sucesso')
                            break

                    if (argumento_usuario[1] == verificador_grupo[1]):
                        if (conexao.validando_tabela_existente(argumento_usuario[2])):
                            print('retornando COnsulta')
                            break
                        else:
                            print('Tabela não existe')

                    if (argumento_usuario[1] == verificador_grupo[2]):
                        if (conexao.validando_tabela_existente(argumento_usuario[2])):
                            print('Deletado com sucesso')
                            break
                        else:
                            print('Tabela não existe')
                else:
                    print('\033[1;31mCOMANDO INVALIDO')
            except ValueError as erro:
                print('\033[1;31mCOMANDO INVALIDO')
            except IndexError as erro:
                print('\033[1;31mCOMANDO INVALIDO')

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


class ArgumentosUsuario:
    def controla_fluxo_argumento(argumento, *args):
        pass

    def argumentos_grupo():
        pass

    def sub_argumentos():
        pass

    def argumento_main():
        pass


estrutura = EstruturaMain
estrutura.main()
