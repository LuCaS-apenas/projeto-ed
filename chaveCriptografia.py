class ChaveCriptografia:

    def __init__(self, chave: str, criacao: datetime, validade: datetime):
        self.chave = chave
        self.criacao = criacao
        self.validade = validade    
        
    @property
    def chave(self):
        return self.__chave
    
    @chave.setter
    def chave(self, chave):
        self.__chave = chave

    @property
    def criacao(self):
        return self.__criacao
    
    @criacao.setter
    def criacao(self, criacao):
        self.__criacao = criacao

    @property
    def validade(self):
        return self.__validade
    
    @criacao.setter
    def validade(self, validade):
        self.__validade = validade

        
    

    def __str__(self):
        return f'''
    Chave: {self.chave}
    Criada em: {self.criacao}
    Expira em: {self.validade}
    '''
