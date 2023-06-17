import datetime
import random
import cryptocode
import sys
from Lista import *
from Arvore import *

class Diretorio:

    def __init__(self, nome: str):
        self.nome = nome
        # self.lista_arquivos = ListaEncadeada()
        self.diretorios = ListaEncadeada()

    # def adicionar_arquivo(self, arquivo):
    #     self.lista_arquivos.inserir_no_inicio ( arquivo )

    def adicionar_diretorio(self, diretorio):
        self.diretorios.inserir_no_inicio(diretorio)

    def listar_tudo(self):
        print(f"--- Diretório: {self.nome} ---")
        self.lista_arquivos.imprime_lista()
        print()

    def __str__(self):
        return f'{self.nome}'

class Arquivo:

    def __init__(self, nome: str, tipo: str, descricao: str, conteudo: str, diretorio: Diretorio):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        time = str ( datetime.datetime.now () )
        self.tamanho = f'{sys.getsizeof ( conteudo )} Bytes'
        self.conteudo = conteudo
        self.criacao = f'''Criado em: {time[8:10]}-{time[5:7]}-{time[0:4]} às {time[11:19]} '''
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

    def __init__(self, chave: str):
        self.chave = chave
        time = str(datetime.datetime.now())
        validade = str(datetime.datetime.now() + datetime.timedelta(days=30))
        self.criacao = f'''Criado em: {time[8:10]}-{time[5:7]}-{time[0:4]} às {time[11:19]} '''
        self.validade = f'''Chave Expira em: {validade[8:10]}-{validade[5:7]}-{validade[0:4]} às {validade[11:19]} '''


    def __str__(self):
        return f'''
    Chave: {self.chave}
    Criada em: {self.criacao}
    Expira em: {self.validade}
    '''

## Árvore Binária
class No:

    def __init__(self, carga: object = None, esquerda: 'No' = None, direita: 'No' = None):
        self.carga = carga
        self.esquerda = esquerda
        self.direita = direita
        self.altura = 1
        self.lista_arquivos = ListaEncadeada()

    def adicionar_arquivo(self, arquivo):
        self.lista_arquivos.inserir_no_inicio(arquivo)

    def imprimir(self, pasta: No = None , indent = 0):

        print(" " * indent + str(self.carga))
        # vai imprimir a lista de arquivos em cada nó que são pastas ou diretorios
        self.lista_arquivos.imprime_lista()
        if self.esquerda:
            self.esquerda.imprimir(indent + 2)
        if self.direita:
            self.direita.imprimir(indent + 2)





    def __str__(self):
        return str(self.carga)

RAIZ = "raiz"
class SistemaDeArquivos:

    def __init__(self, raiz: 'No'):
        self.raiz = raiz

    def pos_ordem(self, no: 'No' = RAIZ):
        if no == RAIZ:
            no = self.raiz
        if no is None:
            return no
        if no.esquerda:
            self.pos_ordem(no.esquerda)
        if no.direita:
            self.pos_ordem(no.direita)
        print(no, end=" ")

    def em_ordem(self, no: 'No' = RAIZ):
        if no == RAIZ:
            no = self.raiz
        if no is None:
            return no
        if no.esquerda:
            self.em_ordem(no.esquerda)
        print(no, end=" ")
        if no.direita:
            self.em_ordem(no.direita)

    def pre_ordem(self, no: 'No' = RAIZ):
        if no == RAIZ:
          no = self.raiz
        if no == None:
          return no
        print(no, end=" ")
        if no.esquerda:
          self.pre_ordem(no.esquerda)
        if no.direita:
          self.pre_ordem(no.direita)

    def imprimir(self):
        self.raiz.imprimir()

    def inserir(self, carga, raiz=RAIZ):
        if raiz == RAIZ:
          raiz = self.raiz

        ## Passo 1 - Inserção normal de uma árvore binária de busca
        if not raiz:
          return No(carga)
        elif carga < raiz.carga:
          raiz.esquerda = self.inserir(carga, raiz.esquerda)
        else:
          raiz.direita = self.inserir(carga, raiz.direita)

        return raiz

    def gerar_chave_criptografia (self, chave):
        chave = ChaveCriptografia(chave)
        return chave

    def revogar_chave_criptografia(self):
        pass

    def listar_diretorios(self, diretorio: Diretorio = None):

        self.raiz.imprimir(diretorio)



    def gravar_arquivo_cifrado(self, diretorio: Diretorio, arquivo: Arquivo):
        pass

    def listar_arquivos(self, pesquisa_diretorio: str):
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

a = SistemaDeArquivos(1)
b = a.gerar_chave_criptografia('123')
print(b)
print(b.chave)

conteudo_do_arquivo = 'Conteudo do arquivo'
senha_criptografada = cryptocode.encrypt(conteudo_do_arquivo, b.chave)


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

diretorio = Diretorio('Diretorio Principal')
subdiretorio1 = Diretorio('Projeto')
subdiretorio2 = Diretorio('Mateus')
subdiretorio3 = Diretorio('Lucas')
subdiretorio4 = Diretorio('Ramon')
subdiretorio5 = Diretorio('Diego')
subdiretorio6 = Diretorio('Gerenciamento')


diretorio_raiz = No(diretorio)
no2diretorio = No(subdiretorio1)
no2diretorio.esquerda = No(subdiretorio2)
no2diretorio.direita = No(subdiretorio3)
diretorio_raiz.esquerda = no2diretorio
no3diretorio = No(subdiretorio4)
no3diretorio.direita = No(subdiretorio5)
no3diretorio.esquerda = No(subdiretorio6)
diretorio_raiz.direita = no3diretorio

a  = SistemaDeArquivos(diretorio_raiz)
a.pre_ordem()


a0 = Arquivo('Arquivo1','txt','senhas',senha_criptografada,subdiretorio1)
a1 = Arquivo('Arquivo2','txt','senhas',senha_criptografada,subdiretorio1)
a2 = Arquivo('Arquivo2','txt','senhas',senha_criptografada,subdiretorio2)
a3 = Arquivo('Arquivo2','txt','senhas',senha_criptografada,subdiretorio3)
a4 = Arquivo('Arquivo2','txt','senhas',senha_criptografada,subdiretorio3)



print()
print('-------------------------')

print()
print()
print('FORMATO DA ARVORE')

print()

# print('Nome do diretorio do arquivo = ',arquivo.diretorio)
print('--------------------------------------------------------')
# Foi modificado o nó da árvore e adicionado uma lista que representa os
# conjuntos de arquivos.
# Em seguida foi modificado o método de imprimir da árvore, acrescentando
# o método de listar em cada nó, assim imprimindo todos os arquivos contidos neles
no2diretorio.adicionar_arquivo(a1)
no2diretorio.esquerda.adicionar_arquivo(a2)
no2diretorio.direita.adicionar_arquivo(a3)
no2diretorio.direita.adicionar_arquivo(a4)
a.imprimir()
