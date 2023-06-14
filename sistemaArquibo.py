import datetime
from chaveCriptografia import ChaveCriptografia
from arquivo import *

class SistemaArquivos:

    def __init__(self, chave: ChaveCriptografia):
        self.chave_criptografia = chave

    @property 
    def chave_criptografia(self):
        return self.__chave_criptografia
    
    @chave_criptografia.setter
    def chave_criptografia(self, chave):
        self.__chave_criptografia = chave

    # função para gerar uma senha para acessar o arquivo.
    def gerar_chave_criptografia(self, chave):
        data_validade = datetime.datetime.now() + datetime.timedelta(days=30)
        data_criacao = datetime.datetime.now()
        return ChaveCriptografia(chave, data_criacao, data_validade)

    def revogar_chave_criptografia(self):
        pass

    def listar_diretorios(self,):
        pass

    def gravar_arquivo_cifrado(self, arquivo: Arquivo):
        pass

    def listar_arquivos(self, diretorio: str):
        pass

    def buscas_arquivo(self, palavra_chave: str, lista_arquivo):
        pass

    def decifrar_arquivo(self, diretorio: str, nome: str):
        pass
