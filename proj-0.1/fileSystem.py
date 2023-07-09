from encryptionKey import *
from file import *
from directory import *
import cryptocode

class FileSystem:
    def __init__(self) -> None:
        self.encryption_key = None

    def generate_encryption_key(self, key: str) -> EncryptionKey:
        
        self.encryption_key = EncryptionKey(key)
    
    def revoke_encryption_key(self, key: str) -> bool : 

        assert (self.encryption_key != key), "Invalid Encryption key entred."

        self.encryption_key = None
        return True

    def list_directories(self, tree: object) -> str:
        tree.pre_order()
        
    def save_encrypted_file(self, name: str, type: str, 
                            description: str, content: str,
                            size: str, directory: Directory) -> File:
        
        if datetime.datetime.now () >= self.encryption_key.expiration:
            print ( f"""
        The password deadline has expired. Please update your password. 
        System-Generated Password Suggestion: {self.senhas_sugeridas ()}
        """ )

        newFile = File (
            name,
            type,
            description,
            cryptocode.encrypt ( content, self.encryption_key.key ),
            size,
            directory )

        directory.files.append ( newFile )

    def list_files(self, directory: Directory) -> list:
        for i in (directory.files):
            print(f"""
                name: {i}
                content: {i.content}""")

    def search_file(self, tree: object, key_word: str) -> list:
        out = tree.pre_order_2(key_word)
        print(out)
        if out == None:
            print(-1)
            return
        print(f"""
                name: {str(out)}
                content: {str(out.content)}""")

        

    def decrypt_file(self, directory: Directory, name: str) -> File:
        
        f = None
        
        for i in range(len(directory.files)):
            if directory.files[i].name == name:
                f =  directory.files[i]
        
        f.content = cryptocode.decrypt(str(f.content), self.encryption_key.key)
        
        return
       
