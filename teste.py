import datetime
import cryptocode
import sys
from Lista import *


class CaracteresInsuficiente(Exception):
    pass

class DiretorioError(Exception):
    pass

class ArquivoError(Exception):
    pass

class Diretorio:

    def __init__(self, nome: str):
        self.nome = nome

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

    def __init__(self, carga: Diretorio = None, esquerda: 'No' = None, direita: 'No' = None):
        self.carga = carga
        self.esquerda = esquerda
        self.direita = direita
        self.altura = 1
        self.lista_arquivos = ListaEncadeada()

    def adicionar_arquivo(self, arquivo):
        self.lista_arquivos.inserir_no_inicio(arquivo)

    def imprimir(self, indent = 0):

        print(" - " * indent + f"{self.carga}")


        # vai imprimir a lista de arquivos em cada nó que são pastas ou diretorios
        # quando o chamar o método de imprimir os nós, que no projeto vai ser diretórios
        # toda vez que a informação de um nó for impresso vai ser listado os arquivos presentes neles.
        self.lista_arquivos.imprime_lista() # modificação

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

    def buscar_arquivo(self, palavra_chave: str, lista_arquivo: No):
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

if __name__ == '__main__':

    print('--------------------------DIRETORIOS------------------------------')

    diretorio = Diretorio('Diretorio Home')
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


    a0 = Arquivo('Arquivo1','txt','senhas','1932932329',diretorio)
    a1 = Arquivo('Arquivo2','txt','senhas','jashdj2h13123',subdiretorio1)
    a2 = Arquivo('Arquivo2','txt','senhas','ughahe23u1412',subdiretorio2)
    a3 = Arquivo('Arquivo2','txt','senhas','kasjdkj12311',subdiretorio3)
    a4 = Arquivo('Arquivo2','txt','senhas','ashjdkahsudu213',subdiretorio3)



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
    # no2diretorio.adicionar_arquivo(a1)
    # no2diretorio.esquerda.adicionar_arquivo(a2)
    # no2diretorio.esquerda.adicionar_arquivo(a3)
    # no2diretorio.direita.adicionar_arquivo(a4)
    #---------------------------------------------------------#
    # teste listagem de diretorios
    # listando a partir de um diretorio específico
    a.listar_diretorios(no2diretorio.direita)
    print('-----------------------------------------')
    # lista tudo é só fornecer o nó da árvore que faz referência o diretorio raiz
    a.listar_diretorios(diretorio_raiz)

    a.gravar_arquivo_cifrado(no3diretorio.esquerda, a0)
    a.gravar_arquivo_cifrado(diretorio_raiz,a1)
    a.gravar_arquivo_cifrado(no2diretorio.direita, a2)

    a.listar_diretorios(diretorio_raiz)

    # passar o nome do diretorio da busca e o local de onde que começar a busca.
    print(a.buscar_diretorio('Mateus',diretorio_raiz))



print('-------------------------------------------------------------------------------------------------------')
    # # é feito uma chamada recursiva para buscar o nome do diretorio na árvore de diretórios.
    # diretorio = self.buscar_diretorio ( diretorio.carga.nome, diretorio )
    # # Se não for encontrado o diretório na árvore, vai ser criado um diretório e inserido na árvore utilizando o método de inserção da árvore binária.
    # if diretorio is None:
    #     novo_diretorio = No ( diretorio.carga.no )
    #     self.inserir ( novo_no, self.raiz )
    #     diretorio = novo_diretorio
