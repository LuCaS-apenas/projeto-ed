class SistemaArquivos:

    def __init__(self, chave: ChaveCriptografia):
        self.chave_criptografia = chave

    # função para gerar uma senha para acessar o arquivo.
    def gerar_chave_criptografia(self):
        caracteres = ''
        while len ( caracteres ) != 11:
            x = random.choice ( 'abcdefghijklmnopqrstuxyzABCDEFGHIJKLMNOPQRSTUVXTZ123456789#@!%¨&*' )
            caracteres += x
        return caracteres

    def revogar_chave_criptografia(self):
        pass

    def listar_diretorios(self):
        pass

    def gravar_arquivo_cifrado(self, arquivo: Arquivo):
        pass

    def listar_arquivos(self, diretorio: str):
        pass

    def buscas_arquivo(self, palavra_chave: str, lista_arquivo):
        pass

    def decifrar_arquivo(self, diretorio: str, nome: str):
        pass
