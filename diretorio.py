class Diretorio:

    def __init__(self, nome: str):
        self.nome = nome
        # self.arqs = []
        
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def __str__(self):
        return f'{self.nome}'
      
