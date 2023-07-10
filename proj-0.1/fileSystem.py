from encryptionKey import *
from file import *
from directory import *
import cryptocode
import random


class FileSystem:
    def __init__(self) -> None:
        self.encryption_key = None
        
    def menu(self):
        return f""" 
    {'-=' * 50}
                                       ENCRYPTED FILE SYSTEM
                   +------+------+------+-----+------+-----+----+-----+-------+  
                   |                                                          |
                   +              ROOT     DOCS    MEDIA    TCC               +
                   |                                                          |
                   +                     FOTOS     VIDEOS                     +
                   |                                                          |
                   +------+------+-----+-----+-----+-----+-----+------+-------+
            
                                                         
            1. View File Structure
            2. Revoke Password
            3. generate encryption key / Save Encrypted File
            4. List Files
            5. decrypt File
            6. Search File
            10.Exit the program.

    {'-=' * 50}
    """
        
    def generate_encryption_key(self, key: str) -> EncryptionKey:
        
        if not isinstance(key, str):
            print("The Encryption key must be a str")
            return
        self.encryption_key = EncryptionKey(key)
        print("Encryption key generated sucessfuly.")
    
    def revoke_encryption_key(self, key: str) -> bool : 
        if self.encryption_key.key == key:
            self.encryption_key = None
            print("Encryption key revoked sucessfuly.")
            return True
        else:
            print("Invalid Encryption key entered.")
            return

    def list_directories(self, tree: object) -> str:
        tree.pre_order()
        
    def suggested_passwords(self):
        password = ''
        for i in range ( 11 ):
            i = random.choice ( '1234567890abcdefghijklmnoprstuvxz!@#$%' )
            password += i
        return password
        
    def save_encrypted_file(self, name: str, type: str, 
                            description: str, content: str,
                            size: str, directory: Directory) -> File:
        
        if self.encryption_key == None:
            print("The encryption key does not exist. Generate a new key to save a file.")
            return

        if datetime.datetime.now () >= self.encryption_key.expiration:
            print ( f"""
        The password deadline has expired. Please update your password. 
        System-Generated Password Suggestion: {self.suggested_passwords ()}
        """ )
            return

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
        tree.pre_order_2(key_word)
        # out = tree.pre_order_2(key_word)
        # print(out)
        # if out == None:
        #     print(-1)
        #     return
        # print(f"""
        #         name: {str(out)}
        #         content: {str(out.content)}""")


    def decrypt_file(self, directory: Directory, name: str) -> File:
    
        f = None
        
        for i in range(len(directory.files)):
            if directory.files[i].name == name:
                f =  directory.files[i]
        
        if f == None:
            print("Directory or file does not exist.")
            return
    
        f.content = cryptocode.decrypt(str(f.content), self.encryption_key.key)
        return
