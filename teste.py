import datetime
import random
import cryptocode
import sys
from Lista import *
from Arvore import *

class Diretorio:

    def __init__(self, nome: str):
        self.nome = nome
        self.subdiretorios = [ ]

    def adicionar_subdiretorio(self, subdiretorio):
        self.subdiretorios.append ( subdiretorio )

    def __str__(self):
        return f'{self.nome}'

class Arquivo:

    def __init__(self, nome: str, tipo: str, descricao: str, conteudo: str, diretorio: Diretorio):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.tamanho = f'{sys.getsizeof ( conteudo )} Bytes'
        self.conteudo = conteudo
        self.criacao = datetime.datetime.now()
        self.diretorio = diretorio.nome

    def __str__(self):
        return f'''
        Diretório: {self.diretorio}
        Arquivo: {self.nome}.{self.tipo}
        Criado em: {self.criacao}
        Tamanho: {self.tamanho}
        Senha: {self.conteudo}
        '''

class ChaveCriptografia:

    def __init__(self, chave: str, validade: datetime):
        self.chave = chave
        self.criacao = datetime.datetime.now()
        self.validade = validade


    def __str__(self):
        return f'''
    Chave: {self.chave}
    Criada em: {self.criacao}
    Expira em: {self.validade}
    '''

class SistemaArquivos(ArvoreBinaria):

    def __init__(self, chave: ChaveCriptografia):
        self.chave_criptografia = chave

    # função para gerar uma senha para acessar o arquivo.
    def gerar_chave_criptografia(self, chave):
        data_validade = datetime.datetime.now() + datetime.timedelta(days=30)
        return ChaveCriptografia(chave, data_validade)

    def revogar_chave_criptografia(self):
        pass

    def listar_diretorios(self, diretorio = None):
       pass

    def gravar_arquivo_cifrado(self, diretorio: Diretorio, arquivo: Arquivo):
        pass

    def listar_arquivos(self, diretorio: str):
        pass

    def buscas_arquivo(self, palavra_chave: str, lista_arquivo):
        pass

    def decifrar_arquivo(self, diretorio: str, nome: str):
        pass

# def criar_arquivo(self):
#     with open ( f'{self.nome}.txt', 'a' ) as arquivo:
#         arquivo.write (f'senha:{self.conteudo}')

# diretorio = Diretorio('Projeto')
# diretorio1 = Diretorio('Teste')
# diretorio2 = Diretorio('Mateus')
# diretorio3 = Diretorio('Lucas')
# diretorio4 = Diretorio('Ramon')

chave = 'abc'
escolha_uma_senha = input('Senha: ')
senha_criptografada = cryptocode.encrypt(escolha_uma_senha, chave)
# a = Arquivo('A','txt','senhas', senha_criptografada, diretorio)
# escolha_uma_senha1 = input('Senha: ')
# senha_criptografada1 = cryptocode.encrypt(escolha_uma_senha1, chave)
# a1 = Arquivo('B','txt','senhas', senha_criptografada1,diretorio1)
# lista = ListaEncadeada()
# lista.inserir_no_inicio(a)
# lista.inserir_no_inicio(a1)
# lista.imprime_lista()
#
#
# print(cryptocode.decrypt(senha_criptografada,chave))
# print(cryptocode.decrypt(senha_criptografada1,chave))
#
#
# def criar_arquivo(x):
#     with open ( f"arquivo_criptografado.txt", 'a' ) as arquivo:
#         arquivo.write (str (x) )
#
# criar_arquivo(a)
print('--------------------------DIRETORIOS------------------------------')
diretorio = Diretorio('Projeto')
diretorio1 = Diretorio('Teste')
diretorio2 = Diretorio('Mateus')
diretorio3 = Diretorio('Lucas')
diretorio4 = Diretorio('Ramon')
diretorio5 = Diretorio('Diego')
diretorio6 = Diretorio('Gerenciamento')

diretorio_raiz = No(diretorio)
no2diretorio = No(diretorio1)
no2diretorio.esquerda = No(diretorio2)
no2diretorio.direita = No(diretorio3)
diretorio_raiz.esquerda = no2diretorio
no3diretorio = No(diretorio4)
no3diretorio.direita = No(diretorio5)
no3diretorio.esquerda = No(diretorio6)
diretorio_raiz.direita = no3diretorio

arvore  = ArvoreBinaria(diretorio_raiz)
arvore.pre_ordem()

print()
print()
print('FORMATO DA ARVORE')
arvore.imprimir()
print()
arquivo = Arquivo('ProjetoED','txt','senhas',senha_criptografada,diretorio2)
arq1 = Arquivo('lucas','txt','senhas',senha_criptografada,diretorio2)
print(arquivo)
print('Nome do diretorio do arquivo = ',arquivo.diretorio)
print(arq1)


