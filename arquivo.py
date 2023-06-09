import sys
import datetime

class Arquivo:

    def __init__(self, nome: str, tipo: str, descricao: str, conteudo: str, diretorio: Diretorio):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.tamanho = f'{sys.getsizeof ( conteudo )} Bytes'
        self.conteudo = conteudo
        self.criacao = datetime.datetime.now()
        self.diretorio = diretorio.nome

    def criar_arquivo(self):
        with open ( f'{self.nome}.txt', 'a' ) as arquivo:
            arquivo.write (f'senha:{self.conteudo}')

    def __str__(self):
        return f'''
        Diretório: {self.diretorio}
        Arquivo: {self.nome}.{self.tipo}
        Criado em: {self.criacao}
        Tamanho: {self.tamanho}
        Senha: {self.conteudo}
        '''
