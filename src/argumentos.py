from interface import Interface


class ArgumentosUsuario:

    def main():
        pass

    def sub_argumentos_add(nome_funcao):

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
