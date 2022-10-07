from pyodbc import ProgrammingError
from datetime import datetime
from interface import Interface
import conexao

cx = conexao.GrupoConexao
comandos = conexao.ArgumentosGrupoSQL
data = datetime.now()


class ArgumentosUsuario:

    def sub_argumentos_add(argumento):
        try:

            if conexao.validando_tabela_existente(argumento[2]):
                descricao = ' '.join(argumento[4:argumento.index('>')])
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
            pass
        except:
            pass

    def sub_argumentos_alter(argumento):
        try:
            pass
        except:
            pass

    def sub_argumentos_complete(argumento):
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


verificador_sub_argumento = ['ADD', 'DELETE', 'ALTER', 'COMPLETE']

executa_funcao = ArgumentosUsuario


def filtra_argumento(argumento):
    match argumento[1]:
        case 'ADD':
            executa_funcao.sub_argumentos_add(argumento)
        case 'DELETE':
            executa_funcao.sub_argumentos_delete(argumento)
        case 'ALTER':
            executa_funcao.sub_argumentos_alter(argumento)
        case 'COMPLETE':
            executa_funcao.sub_argumentos_complete(argumento)
