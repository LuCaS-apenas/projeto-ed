class No:

    def __init__(self, carga: 'No' = None, prox: 'No' = None):
        self.carga = carga
        self.proximo = prox

    def __str__(self):
        return str (self.carga)

class ListaEncadeada:

    def __init__(self):
        self.cabeca:'No' = None
        self.cauda:'No' = None

    def inserir_no_inicio(self, carga):
        valor: No = No(carga)
        if self.cabeca is None:
            self.cabeca = valor
            self.cauda = valor
        else:
            valor.proximo = self.cabeca
            self.cabeca = valor

    def inserir_no_final(self, valor):
        value: No = No(valor)
        if self.cabeca is None:
            self.cauda = value
            self.cabeca = value
        # se não, o próximo valor tera o resultado da cabeça, e o valor atual da cabeça
        # será o valor inserido
        else:
            self.cauda.proximo = value
            self.cauda = value

    def remover_no_inicio(self):
        if self.cabeca is None:
            print('Lista Vazia!')
            return

        if self.cabeca == self.cauda:
            self.cabeca = None
            self.cauda = None

        else:
            self.cabeca = self.cabeca.proximo

    def remover_no_final(self):
        if self.cabeca is None:
            print('Lista Vazia!')
            return

        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None

        else:
# Atribuo o valor da cabeça em uma variavel para poder manipular a lista
# enquanto o valor atual da cabeca não for a cauda vai está em loop infinito.
# Quando o valor atual for igual ao valor anterior ao da cauda
# Quebra o loop e o valor atual da cauda vai ser igual ao penultimo valor
# e o proximo valor vai ser None.
            atual = self.cabeca
            while atual.proximo is not self.cauda:
                atual = self.cabeca.proximo

            self.cauda = atual
            atual.proximo = None


    def imprime_lista(self):
        if self.cabeca is None:
            print ( "Lista Vazia" )
            return

        atual: 'No' = self.cabeca
# Vai printar a carga (valor da lista)
# até quando o valor atual for None.
        while atual is not None:
            print(f'{atual.carga}' +  ' ')
            atual = atual.proximo
