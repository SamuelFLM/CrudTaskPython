import logging


logging.basicConfig(level=logging.DEBUG, filename='registro.log',
                    filemode='a', format='%(levelname)s - %(message)s - %(asctime)s')


class Log:

    def log_debug():
        pass

    def log_info():
        pass

    def log_warning():
        pass

    def log_error():
        pass

    def log_critical():
        pass


# Niveis de log
# debug - So estou informando informações para desenvolvedores
# info - So quero informar algo que está acontecendo no programa, mas que nao e um erro.
# warning - Quero alertar sobre algo que está acontecendo, possivelmente fora do esperado, porém ainda nao e um erro.
# error - Um erro ocorreu na aplicação
# critical - Um erro com consequencias graves acaba ocorrer na aplicação
