from pyodbc import ProgrammingError
import argumentos
from verificador import VerificadorTabelas
import os
import time

argumentosUsuario = argumentos
valida_informacao_tabela = VerificadorTabelas


class EstruturaMain:

    def main():
        verificador_executador = ['EX', 'TASK']
        verificador_grupo = ['CREATE', 'READ', 'DELETE', 'DOC']
        while True:
            time.sleep(1)
            os.system('cls')
            try:
                argumento_usuario = input('\033[1;32mDigite: ').upper().split()
                if (argumento_usuario[0] in verificador_executador):

                    # Argumentos Task (Add, delete, complete, alter)
                    if argumento_usuario[0] == verificador_executador[1]:
                        argumentosUsuario.filtra_argumento(
                            argumento_usuario)
                        EstruturaMain.main()

                    # Criação Tabela
                    if (argumento_usuario[1] == verificador_grupo[0]):
                        valida_informacao_tabela.valida_criacao_tabela(
                            argumento_usuario[2])

                    # Ler Tabela ou verfica todas tabelas
                    # EX READ FACULDADE -> TASK DA TABELA
                    # EX READ TABLE -> NOMES DAS TABELAS
                    if (argumento_usuario[1] == verificador_grupo[1]):
                        valida_informacao_tabela.valida_leitura_tabela(
                            argumento_usuario[2])
                        EstruturaMain.main()

                    # Deleta Tabela ou Deleta tarefa
                    if (argumento_usuario[1] == verificador_grupo[2]):
                        valida_informacao_tabela.valida_exclusao_tabela(
                            argumento_usuario[2])

                    # Documentação Grupo ou Sub-Grupo
                    if (argumento_usuario[1] == verificador_grupo[3]):
                        argumentosUsuario.sub_argumentos_doc(
                            argumento_usuario[2])

            except ValueError as erro:
                print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
            except IndexError as erro:
                print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
            except TypeError as erro:
                print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
            except ProgrammingError as erro:
                print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')

    # OK INSERI INFORMAÇÃO TABELA

    # OK LER INFORMAÇÃO
    # comandos.ler_tarefas('faculdade')

    # OK COMPLETAR TAREFAS
    # cx.GrupoConexao.executa_query_sql(comandos.complete_tarefa('faculdade', 1))

    # OK ALTERAR TAREFASs
    # cx.GrupoConexao.executa_query_sql(comandos.alterar_tarefa(
    #     'faculdade', 'descricao', 'Descricao bolada hehe', 1))

    # OK DELETAR TAREFAS
    # cx.GrupoConexao.executa_query_sql(comandos.deleta_tarefa('faculdade', 1))
