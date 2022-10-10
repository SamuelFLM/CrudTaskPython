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

                    # Table(EX)
                    # Lida com argumentos da tabela(Create, Read, Delete)
                    if argumento_usuario[0] == argumento_executador[0]:
                        argumentosUsuario.filtra_argumento_tabela(
                            argumento_usuario)
                        EstruturaMain.main()
                    # Task
                    # Argumentos Task (Add, delete, complete, alter, doc)
                    if argumento_usuario[0] == argumento_executador[1]:
                        argumentosUsuario.filtra_argumento(
                            argumento_usuario)
                        EstruturaMain.main()
                else:
                    print(
                        '\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
            except ValueError as erro:
                print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
            except IndexError as erro:
                print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
            except TypeError as erro:
                print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
            except ProgrammingError as erro:
                print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
