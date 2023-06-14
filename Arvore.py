## Árvore Binária
class No:
  def __init__(self, carga: object, esquerda: 'No' = None, direita: 'No' = None):
    self.carga = carga
    self.esquerda = esquerda
    self.direita = direita
    self.altura = 1

  def imprimir(self, indent = 0):
    print(" " * indent + str(self.carga))
    if self.esquerda:
      self.esquerda.imprimir(indent + 2)
    if self.direita:
      self.direita.imprimir(indent + 2)

  def __str__(self):
    return str(self.carga)

RAIZ = "raiz"
class ArvoreBinaria:
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

  def imprimir(self, no_inicial=None):
    # se o nó inicial for None, vai imprimir todos os nós da árvore recursivamente
    # algum ponto do nó for passado como parâmetro, a impressão da árvore vai partir desse pronto
    if no_inicial is None:
      no_inicial = self.raiz
    no_inicial.imprimir()

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

