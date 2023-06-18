from Lista import *
from ChaveCriptografia import *
from Diretorio import *
from SistemaDeArquivo import *
import cryptocode
import sys

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

    # exemplo de busca de arquivo
    a.buscar_arquivos('Arquivo1', diretorio_raiz.lista_arquivos)

print('-------------------------------------------------------------------------------------------------------')
