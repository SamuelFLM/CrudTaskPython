import conexao
from interface import Interface
from datetime import datetime
import os
import time

cx = conexao.GrupoConexao
comandos = conexao.ArgumentosGrupoSQL


class EstruturaMain:

    def main():
        argumentoUsuario = ArgumentosUsuario
        verificador_grupo = ['CREATE', 'READ', 'DELETE', 'DOC']
        while True:
            time.sleep(1)
            os.system('cls')
            try:
                argumento_usuario = input('\033[1;32mDigite: ').upper().split()
                if (argumento_usuario[1] in verificador_grupo):

                    if (argumento_usuario[1] == verificador_grupo[0]):
                        if (conexao.validando_tabela_existente(argumento_usuario[2])):
                            print('\033[7;31mTABELA JÀ EXISTENTE')
                        else:
                            cx.executa_query_sql(
                                cx.cria_tabela_sql(argumento_usuario[2]))
                            print('Tabela Criada com sucesso')

                    if (argumento_usuario[1] == verificador_grupo[1]):
                        if (conexao.validando_tabela_existente(argumento_usuario[2])):
                            comandos.ler_tarefas(argumento_usuario[2])
                            input('Aperte para continuar......')
                        else:
                            print('\033[1;31mTABELA NÃO EXISTENTE')

                    if (argumento_usuario[1] == verificador_grupo[2]):
                        if (conexao.validando_tabela_existente(argumento_usuario[2])):
                            cx.executa_query_sql(
                                cx.excluir_tabela_sql(argumento_usuario[2]))
                            print('\033[1;32mTABELA DELETADA COM SUCESSO')
                        else:
                            print('\033[1;31mTABELA NÃO EXISTENTE')

                    if (argumento_usuario[1] == verificador_grupo[3]):
                        argumentoUsuario.sub_argumentos_doc(
                            argumento_usuario[2])
                else:
                    print(
                        '\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
            except ValueError as erro:
                print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
            except IndexError as erro:
                print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
            except TypeError as erro:
                print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')

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

    # OK ALTERAR TAREFASs
    # cx.GrupoConexao.executa_query_sql(comandos.alterar_tarefa(
    #     'faculdade', 'descricao', 'Descricao bolada hehe', 1))

    # OK DELETAR TAREFAS
    # cx.GrupoConexao.executa_query_sql(comandos.deleta_tarefa('faculdade', 1))


class ArgumentosUsuario:

    def sub_argumentos(nome_funcao):
        verificador = ['ADD', 'READ', 'DELETE', 'ALTER', 'COMPLETE']
        try:
            pass
        except:
            pass

    def sub_argumentos_doc(nome_funcao):
        verificador = ['GROUP', 'SUB']
        doc = Interface
        try:
            if nome_funcao in verificador:
                if nome_funcao == verificador[0]:
                    doc.documentacao_grupo()
                else:
                    doc.documentacao_sub_comandos()
            else:
                return print('\033[1;31mCOMANDO INVALIDO')
        except ValueError as erro:
            print('\033[1;31mCOMANDO INVALIDO')
        except IndexError as erro:
            print('\033[1;31mCOMANDO INVALIDO')


estrutura = EstruturaMain
estrutura.main()
