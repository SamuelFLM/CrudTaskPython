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
        \033[1;EX CREATE NOME_DO_GRUPO

        \033[1;37m#Mostrar todas as task da tabela
        \033[1;33mEX READ NOME_DO_GRUPO

        \033[1;37m#Deleta um grupo expecifico
        \033[1;33mEX DELETE NOME_DO_GRUPO

        \033[1;37m#Mostra todas as tabelas existentes
        \033[1;33mEX TABLE

        \033[1;37m#Documentacao
        \033[1;37m#GROUP = DOCUMENTAÇÃO DAS TABELAS
        \033[1;37m#SUB = DOCUMENTAÇÃO DAS TASK
        \033[1;33mEX DOC GROUP/SUB
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
        \033[1;33mTem que ter esses espaços < DESCRICAO > [ PRIORIDADE ]
        \033[1;33m [ PRIORIDADE ] Utilizar apenas 1 caracter. ex: [ A ]
        \033[1;33mTASK ADD NOME_TABELA < DESCRICAO > [ PRIORIDADE ]

        \033[1;37m#Leia TASK da tabela
        \033[1;33mTASK READ NOME_TABELA

        \033[1;37m#Deleta uma task da tabela expecifica
        \033[1;33mTASK DELETE NOME_TABELA ID_TAREFA

        \033[1;37m#ALTER altera uma descricao ou propriedade expecifica
        \033[1;33mTASK ALTER NOME_TABELA TIPO_COLUNA(DESCRICAO OU PROPRIEDADE) < NOVA DESCRICAO > OU [ NOVA PRIORIDADE ]
        \033[1;33mEX: TASK ALTER FACULDADE DESCRICAO < ALTERANDO > [ID]
        \033[1;33mEX: TASK ALTER FACULDADE PRORIEDADE < A > [ID]


        \033[1;37m#Complete suas tarefas
        \033[1;33mTASK COMPLETE NOME_TABELA ID_TAREFA
        """)
        sair_doc = input('Aperte enter para continuar.....')
        return sair_doc
