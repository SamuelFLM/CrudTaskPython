import os


class ConfigTela:

    def limpa_tela():
        os.system('cls')

    def titulo(nome_titulo, qtd_caracter):
        print(qtd_caracter * '\033[1;33m*')
        print(f'    \033[1;37m{nome_titulo}   ')
        print(qtd_caracter * '\033[1;33m*')


tela = ConfigTela


class Interface:
    def documentacao_grupo():
        tela.limpa_tela()
        tela.titulo('DOCUMENTACAO GRUPO', 30)
        print("""
        \nCOMANDOS GRUPOS
        \033[1;37m#Cria uma lista unica para determinado tipo de tarefa.
        \033[1;33mTASK CREATE NOME_DO_GRUPO

        \033[1;37m#Leia um grupo expecifico
        \033[1;33mTASK READ NOME_DO_GRUPO

        \033[1;37m#Deleta um grupo expecifico
        \033[1;33mTASK DELETE NOME_DO_GRUPO
        """)
        sair_doc = input('Aperte enter para continuar.....')
        return sair_doc

    # A fazer
    def documentacao_sub_comandos():
        tela.limpa_tela()
        tela.titulo('DOCUMENTACAO SUB-COMANDOS', 30)
        print("""
        \nSUB-COMANDOS 
        \033[1;37m#Cria uma lista unica para determinado tipo de tarefa.
        \033[1;33mTASK ADD [DESCRICAO] 

        \033[1;37m#Leia um grupo expecifico
        \033[1;33mTASK READ NOME_DO_GRUPO

        \033[1;37m#Deleta um grupo expecifico
        \033[1;33mTASK DELETE NOME_DO_GRUPO

        \033[1;37m#Deleta um grupo expecifico
        \033[1;33mTASK ALTER NOME_DO_GRUPO

        \033[1;37m#Deleta um grupo expecifico
        \033[1;33mTASK COMPLETE NOME_DO_GRUPO
        """)
        sair_doc = input('Aperte enter para continuar.....')
        return sair_doc

    def home():
        pass
