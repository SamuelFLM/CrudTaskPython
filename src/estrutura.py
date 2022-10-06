from argumentos import ArgumentosUsuario
from verificador import VerificadorTabelas
import os
import time


argumentosUsuario = ArgumentosUsuario
valida_informacao_tabela = VerificadorTabelas


class EstruturaMain:

    def main():
        verificador_grupo = ['CREATE', 'READ', 'DELETE', 'DOC']
        verificador_sub_argumento = [
            'ADD', 'READ', 'DELETE', 'ALTER', 'COMPLETE']
        while True:
            time.sleep(1)
            os.system('cls')
            try:
                argumento_usuario = input('\033[1;32mDigite: ').upper().split()
                if (argumento_usuario[1] in verificador_grupo):

                    # Criação Tabela
                    if (argumento_usuario[1] == verificador_grupo[0]):
                        valida_informacao_tabela.valida_criacao_tabela(
                            argumento_usuario[2])

                    # Ler Tabela
                    if (argumento_usuario[1] == verificador_grupo[1]):
                        valida_informacao_tabela.valida_leitura_tabela(
                            argumento_usuario[2])

                    # Deleta Tabela
                    if (argumento_usuario[1] == verificador_grupo[2]):
                        valida_informacao_tabela.valida_exclusao_tabela(
                            argumento_usuario[2])

                    # Documentação Grupo ou Sub-Grupo
                    if (argumento_usuario[1] == verificador_grupo[3]):
                        argumentosUsuario.sub_argumentos_doc(
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


estrutura = EstruturaMain
estrutura.main()
