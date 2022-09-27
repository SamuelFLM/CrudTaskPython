import os


class ConfigTela:

    def limpa_tela():
        os.system('cls')

    def titulo(nome_titulo, qtd_caracter):
        print(qtd_caracter * '*')
        print(f'    {nome_titulo}   ')
        print(qtd_caracter * '*')


tela = ConfigTela


class Interface:
    def documentacao_grupo():
        tela.limpa_tela()
        tela.titulo('DOCUMENTAÇAO GRUPO', 30)
        print("""
        \nCOMANDOS GRUPOS
        #Cria uma lista unica para determinado tipo de tarefa.
        TASK CREATE NOME_DO_GRUPO

        #Leia um grupo expecifico
        TASK READ NOME_DO_GRUPO

        #Deleta um grupo expecifico
        TASK DELETE NOME_DO_GRUPO
        """)
        sair_doc = input('Aperte enter para continuar.....')
        return sair_doc

    # A fazer
    def documentacao_sub_comandos():
        tela.limpa_tela()
        tela.titulo('DOCUMENTAÇAO SUB-COMANDOS', 30)
        print("""
        \nSUB-COMANDOS 
        #Cria uma lista unica para determinado tipo de tarefa.
        TASK ADD 

        #Leia um grupo expecifico
        TASK READ NOME_DO_GRUPO

        #Deleta um grupo expecifico
        TASK DELETE NOME_DO_GRUPO
        """)
        sair_doc = input('Aperte enter para continuar.....')
        return sair_doc

    def home():
        pass
