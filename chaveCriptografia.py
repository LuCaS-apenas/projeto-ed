
class ChaveCriptografia:

    def __init__(self, chave: str):
        self.chave = chave
        time = str(datetime.datetime.now())
        validade = str(datetime.datetime.now() + datetime.timedelta(days=30))
        self.__criacao = f'''Criado em: {time[8:10]}-{time[5:7]}-{time[0:4]} às {time[11:19]} '''
        self.__validade = f'''Chave Expira em: {validade[8:10]}-{validade[5:7]}-{validade[0:4]} às {validade[11:19]} '''


    @property
    def criacao(self):
        return self.__criacao

    @property
    def validade(self):
        return self.__validade

    @property
    def chave(self):
        return self.__chave

    @chave.setter
    def chave(self, nova):
        self.__chave = nova

    def __str__(self):
        return f'''
    Chave: {self.chave}
    Criada em: {self.criacao}
    Expira em: {self.validade}
    '''
