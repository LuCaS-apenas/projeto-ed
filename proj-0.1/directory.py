class Directory:

    def __init__(self, name: str):
        self.name = name
        self.files = []
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def files(self):
        return self.__files
    
    @files.setter
    def files(self, files):
        assert all(isinstance(f, str) for f in files), 'files must be strings.'
        self.__files = files
    
    def __str__(self):
        return f'{self.name}'
      