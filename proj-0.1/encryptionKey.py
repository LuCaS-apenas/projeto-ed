import datetime

class EncryptionKey:

    def __init__(self, key: str):
        self.key = key
        self.creation = datetime.datetime.now()
        self.expiration = datetime.datetime.now() + datetime.timedelta(days=30)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    def __str__(self):
        return f'''
    key: {self.key}
    creation date: {self.creation}
    expiration date: {self.expiration}
    '''
