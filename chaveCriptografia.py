class ChaveCriptografia:

    def __init__(self, chave: str, criacao: datetime, validade: datetime):
        self.chave = chave
        self.criacao = criacao
        self.validade = validade

    def __str__(self):
        return f'''
    Chave: {self.chave}
    Criada em: {self.criacao}
    Expira em: {self.validade}
    '''
