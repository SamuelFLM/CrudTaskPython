from pyodbc import ProgrammingError
from datetime import datetime
from interface import Interface
from verificador import VerificadorTabelas
import conexao

cx = conexao.GrupoConexao
comandos = conexao.ArgumentosGrupoSQL
verif = VerificadorTabelas
data = datetime.now()


class ArgumentosUsuario:

    def sub_argumentos_add(argumento):
        try:
            if conexao.validando_tabela_existente(argumento[2]):
                descricao = (' ').join(argumento[4:argumento.index('>')])
                prioridade = (' ').join(
                    argumento[argumento.index('['): argumento.index(']')][1])
                if (len(prioridade) == 1) and (descricao != False):
                    cx.executa_query_sql(comandos.adicionar_tarefa(
                        argumento[2], descricao, prioridade, 'NO', data.__format__('%d/%m/%Y %H:%M:%S'), None))
                    print('\033[1;32mTAREFA ADICIONADA COM SUCESSO ')

        except ProgrammingError as erro:
            print('\033[1;31mERRO PARA ADICIONAR TASK')
        except ValueError as erro:
            print('\033[1;31mVALOR DIGITADO INCORRETAMENTE')
        except IndexError as erro:
            print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
        except TypeError as erro:
            print('\033[1;31mERRO ESCRITA')

    def sub_argumentos_delete(argumento):
        try:
            if (conexao.validando_tabela_existente(argumento[2])):
                if (conexao.valida_se_existe_task_na_tabela(argumento[2], argumento[3])):
                    cx.executa_query_sql(comandos.deleta_tarefa(
                        argumento[2], argumento[3]))
                    print('\033[1;32mTABELA DELETADA COM SUCESSO')
                else:
                    print('\033[1;31mID NÃO ENCONTRADO')
            else:
                print('\033[1;31mTABELA NÃO EXISTENTE')
        except ValueError as erro:
            print('\033[1;31mCOMANDO INVALIDO')
        except IndexError as erro:
            print('\033[1;31mCOMANDO INVALIDO')

    def sub_argumentos_alter(argumento):
        try:
            argumentos = ['DESCRICAO', 'PRIORIDADE']
            if conexao.validando_tabela_existente(argumento[2]):
                descricao = (' ').join(argumento[4:argumento.index('>')])
                id = argumento[argumento.index('['): argumento.index(']')][1]
                if (argumento[3] in argumentos):
                    cx.executa_query_sql(comandos.alterar_tarefa(
                        argumento[2], argumento[3], descricao, id))
                    print('\033[1;32mTAREFA ALTERADA COM SUCESSO ')
                else:
                    print('\033[1;31mCOMANDO INVALIDO')
            else:
                print('\033[1;31mTABELA NÃO EXISTENTE')
        except ProgrammingError as erro:
            print('\033[1;31mERRO PARA ADICIONAR TASK')
        except ValueError as erro:
            print('\033[1;31mVALOR DIGITADO INCORRETAMENTE')
        except IndexError as erro:
            print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
        except TypeError as erro:
            print('\033[1;31mERRO ESCRITA')

    def sub_argumentos_complete(argumento):
        try:
            if (conexao.validando_tabela_existente(argumento[2])):
                if (conexao.valida_se_existe_task_na_tabela(argumento[2], argumento[3])):
                    cx.executa_query_sql(comandos.complete_tarefa(
                        argumento[2], argumento[3], data.__format__('%d/%m/%Y %H:%M:%S')))
                    print('\033[1;32mTABELA CONCLUIDA COM SUCESSO')
                else:
                    print('\033[1;31mCOMANDO INVALIDO')
            else:
                print('\033[1;31mCOMANDO INVALIDO')
        except ProgrammingError as erro:
            print('\033[1;31mERRO PARA ADICIONAR TASK')
        except ValueError as erro:
            print('\033[1;31mVALOR DIGITADO INCORRETAMENTE')
        except IndexError as erro:
            print('\033[1;31mCOMANDO INVALIDO FAVOR CONSULTAR DOCUMENTACAO')
        except TypeError as erro:
            print('\033[1;31mERRO ESCRITA')

    def sub_argumentos_doc(argumento):
        verificador = ['GROUP', 'SUB']
        doc = Interface
        try:
            if argumento[2] in verificador:
                if argumento[2] == verificador[0]:
                    doc.documentacao_grupo()
                else:
                    doc.documentacao_sub_comandos()
            else:
                return print('\033[1;31mCOMANDO INVALIDO')
        except ValueError as erro:
            print('\033[1;31mCOMANDO INVALIDO')
        except IndexError as erro:
            print('\033[1;31mCOMANDO INVALIDO')


verificador_sub_argumento = ['ADD', 'DELETE', 'ALTER', 'COMPLETE']

executa_funcao = ArgumentosUsuario


def filtra_argumento(argumento):
    match argumento[1]:
        case 'ADD':
            executa_funcao.sub_argumentos_add(argumento)
            input("Aperte enter para continuar.......")
        case 'DELETE':
            executa_funcao.sub_argumentos_delete(argumento)
            input("Aperte enter para continuar.......")
        case 'ALTER':
            executa_funcao.sub_argumentos_alter(argumento)
            input("Aperte enter para continuar.......")
        case 'COMPLETE':
            executa_funcao.sub_argumentos_complete(argumento)
            input("Aperte enter para continuar.......")
        case 'DOC':
            executa_funcao.sub_argumentos_doc(argumento)


def filtra_argumento_tabela(argumento):
    match argumento[1]:
        case 'CREATE':
            verif.valida_criacao_tabela(argumento)
            input("Aperte enter para continuar.......")
        case 'READ':
            verif.valida_leitura_tabela(argumento)
            input("Aperte enter para continuar.......")
        case 'DELETE':
            verif.valida_exclusao_tabela(argumento)
            input("Aperte enter para continuar.......")
        case 'TABLE':
            comandos.read_tabelas()
            input("Aperte enter para continuar.......")
