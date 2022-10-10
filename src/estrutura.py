from pyodbc import ProgrammingError
import argumentos
from verificador import VerificadorTabelas
import os
import time

argumentosUsuario = argumentos
valida_informacao_tabela = VerificadorTabelas


class EstruturaMain:

    def main():
        argumento_executador = ['EX', 'TASK']
        while True:
            time.sleep(1)
            os.system('cls')
            try:
                argumento_usuario = input('\033[1;32mDigite: ').upper().split()
                if (argumento_usuario[0] in argumento_executador):

                    # Lida com argumentos da tabela(Create, Read, Delete)
                    if argumento_usuario[0] == argumento_executador[0]:
                        argumentosUsuario.filtra_argumento_tabela(
                            argumento_usuario)
                        EstruturaMain.main()

                    # Argumentos Task (Add, delete, complete, alter, doc)
                    if argumento_usuario[0] == argumento_executador[1]:
                        argumentosUsuario.filtra_argumento(
                            argumento_usuario)
                        EstruturaMain.main()
                else:
                    pass
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
