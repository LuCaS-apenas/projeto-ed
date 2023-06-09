class Arquivo:

    def __init__(self, nome: str, tipo: str, descricao: str, conteudo: str, criacao: datetime, diretorio:Diretorio, tamanho: int = 0):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.tamanho = tamanho
        self.conteudo = conteudo
        self.criacao = criacao
        self.diretorio = diretorio

    def criar_arquivo(self):
        with open ( self.nome, 'w' ) as arquivo:
            arquivo.write (f'{self.conteudo}')

    def __str__(self):
        return f'''
        Arquivo: {self.nome}.{self.tipo}
        Criado em: {self.criacao}
        Tamanho: {self.tamanho}
        {self.conteudo}
        '''
