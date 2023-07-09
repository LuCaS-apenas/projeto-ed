## Árvore Binária
class No:
  def __init__(self, carga: object, esquerda: 'No' = None, direita: 'No' = None):
    self.carga = carga
    self.esquerda = esquerda
    self.direita = direita
    self.altura = 1

  def imprimir(self, indent = 1):
    print(" " * indent + str(self.carga))
    if self.esquerda:
      self.esquerda.imprimir(indent - 1)
    if self.direita:
      self.direita.imprimir(indent + 2)

  def __str__(self):
    return str(self.carga)

RAIZ = "raiz"
class ArvoreBinaria:
  def __init__(self, raiz: 'No'):
    self.raiz = raiz

  def pre_order(self, no: 'No' = RAIZ, nivel = 0):
    espacos = "|--" * nivel
    if no == RAIZ:
      no = self.raiz
    if no == None:
      return no
    print(espacos + str(no) + "/")
    # print(no.carga.name)
    # print("|")
    for i in no.carga.files:
      print(espacos + "|--" + str(i)) 
    if no.esquerda:
      self.pre_order(no.esquerda, nivel+1)
    if no.direita:
      self.pre_order(no.direita, nivel+1)


class ArvoreAVL(ArvoreBinaria):

  def buscar(self, chave, raiz=RAIZ):
    if raiz == RAIZ:
      raiz = self.raiz

    if raiz is None:
      return None
    
    for i in raiz.carga.files:
     if i.name == chave:
      return i 

    # return self.pre_order_2(raiz)
     if chave > raiz.carga.files[0].name:
      return self.buscar(chave, raiz.direita)

    return self.buscar(chave, raiz.esquerda) 

  def pre_order_2(self, chave, no: 'No' = RAIZ, nivel = 0):
      
    if no == RAIZ:
        no = self.raiz
    if no == None:
      return no

    for i in no.carga.files:
      if i.name == chave:
        print(i)
        return i
      
    if no.esquerda:
        self.pre_order_2(chave, no.esquerda, nivel+1)
    if no.direita:
        self.pre_order_2(chave, no.direita, nivel+1)




