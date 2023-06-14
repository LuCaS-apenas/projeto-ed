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

    def listar_diretorios(self, no = None):
        return ArvoreBinaria.imprimir( no )

    def gravar_arquivo_cifrado(self, arquivo: Arquivo):
        pass

    def listar_arquivos(self, diretorio: str):
        pass

    def buscas_arquivo(self, palavra_chave: str, lista_arquivo):
        #palavra_chave  == nome do arquivo
        for arq in range(len(lista_arquivo)):
            if lista_arquivo[arq] == palavra_chave:
                return arq
            if lista_arquivo[arq] > palavra_chave:
                return "Não encontrado"
        return -1

    def decifrar_arquivo(self, diretorio: str, nome: str):
        pass
