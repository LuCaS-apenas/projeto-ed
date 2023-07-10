## Árvore Binária
class No:
  def __init__(self, carga: object, esquerda: 'No' = None, direita: 'No' = None):
    self.carga = carga
    self.esquerda = esquerda
    self.direita = direita
    self.altura = 1

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

  def pre_order_2(self, chave, no: 'No' = RAIZ):
    
    if no == RAIZ:
        no = self.raiz
    if no == None:
      return no

    for i in no.carga.files:
      if i.name == chave:
        print(f"""
                name: {str(i)}
                content: {str(i.content)}""")

    if no.esquerda:
        self.pre_order_2(chave, no.esquerda)
    if no.direita:
        self.pre_order_2(chave, no.direita)





