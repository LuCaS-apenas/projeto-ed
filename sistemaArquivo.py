import datetime
from chaveCriptografia import ChaveCriptografia
from arquivo import *
import cryptocode
import sys

RAIZ = "raiz"
class SistemaDeArquivos:

    def __init__(self, raiz: 'No'):
        self.raiz = raiz
        self.key = None

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, chave):
        self.__key = chave

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

        # Se o nó inicial for None, vai imprimir todos os nós da árvore recursivamente.
        # Caso algum nó seja passado como parâmetro, a impressão da árvore vai partir desse ponto da árvore.

        if diretorio is None:
            diretorio = self.raiz # diretorio vai ser o ponto inicial da impressão da árvore, no caso vai imprimir tudo a partir do novo nó, cada nó é um diretorio diferente.
        diretorio.imprimir () # o método de impressão da árvore na classe No, foi modificado para imprimir a lista de arquivo presente em cada nó.

    def buscar_arquivos(self, palavra_chave, lista_arquivo):
        pass


    def buscar_diretorio(self, nome: str, diretorio: 'No' = None):

        if diretorio is None:
            return diretorio
        # Se o nome fornecido for igual ao algum diretório, que no caso é o nome do nó da árvore binária.
        # Ira retornar o nó atual.
        if nome == diretorio.carga.nome:
            return diretorio

        # vai verificar se à esquerda da árvore tem elementos.
        if diretorio.esquerda:
            # é utilizado uma variável para armazenar o resultado da busca da chamada recursiva do lado esquerdo da árvore onde estão os diretórios.
            diretorio_encontrado = self.buscar_diretorio ( nome, diretorio.esquerda)
            # se for encontrado alguma coisa irá ser retornado.
            return diretorio_encontrado

        if diretorio.direita:
            diretorio_encontrado = self.buscar_diretorio( nome, diretorio.direita )
            return diretorio_encontrado
        return None

    # está gravando no local certo, mas não está funcionando direito a criação de um novo nó(diretorio) caso ele não exista.
    def gravar_arquivo_cifrado(self, diretorio: No, arquivo: Arquivo):
        # verificações para validar o tipo dos parâmetros fornecidos
        if not isinstance(diretorio, No):
            raise('Precisa fornecer um No valido!')

        if not isinstance(arquivo, Arquivo):
            raise('Precisa fornecer um objeto do tipo arquivo!')

        chave = input('Escolha uma chave: ')

        key = self.gerar_chave_criptografia(chave)

        # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' #

        # ESTÁ FALTANDO IMPLEMENTAR UMA LÓGICA PARA SE O DIRETORIO NÃO EXISTIR, SER CRIADO E INSERIDO NA RAIZ DOS DIRETORIOS.

        # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' #
        self.key = key.chave # varíavel vai ser utilizada pra decifrar o conteúdo do arquivo.

        # É pego o conteúdo do arquivo e usado a biblioteca para cryptografar, passando como parâmetro a mensagem
        # que irá ser criptografada e uma chave.
        arquivo.conteudo = cryptocode.encrypt(arquivo.conteudo, key.chave)
        diretorio.adicionar_arquivo(arquivo)

    def listar_arquivos(self, pesquisa_diretorio: str):
        pass

    # FALTA TERMINAR
    def decifrar_arquivo(self, diretorio: str, arquivo: str, Diretorios: No, lista: No):
        diretorio_encontrado = self.buscar_diretorio( diretorio, Diretorios )
        arquivo_encontrado = self.buscar_arquivo(arquivo, lista.lista_arquivos )

        pass
