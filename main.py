import cryptocode
from Lista import *

diretorio = Diretorio('Projeto')
chave = 'abc'
escolha_uma_senha = input('Senha: ')
senha_criptografada = cryptocode.encrypt(escolha_uma_senha, chave)
a = Arquivo('teste','txt','senhas', senha_criptografada, diretorio)

lista = ListaEncadeada()
lista.inserir_no_inicio(a)
lista.imprime_lista()


def criar_arquivo(x):
    with open ( f"a.txt", 'a' ) as arquivo:
        arquivo.write ( f'senha:{x}' )

criar_arquivo(a)

