from AVLTree import *
from diretory import *
from encryptionKey import *
from file import *
from fileSystem import *
import cryptocode
import time

fileSystem = FileSystem()
fileSystem.generate_encryption_key("asdf")


root = Directory("root")
docs = Directory("docs")
media = Directory("media")
tcc = Directory("tcc")
fotos = Directory("fotos")
videos = Directory("videos")

dirRoot = No(root)
dirDocs = No(docs)
dirMedia = No(media)
dirTcc = No(tcc)
dirFotos = No(fotos)
dirVideos = No(videos)

dirRoot.esquerda = dirDocs
dirRoot.direita = dirMedia
dirDocs.direita = dirTcc
dirMedia.direita = dirFotos
dirMedia.esquerda = dirVideos


arvore = ArvoreAVL(dirRoot)


fileSystem.save_encrypted_file("artigo","txt","meu amor", "aaaa", 34, docs)
fileSystem.save_encrypted_file("café","txt","meu amor", "aaaa", 34, root)
fileSystem.save_encrypted_file("amor","txt","meu amor", "aaaa", 34, root)
fileSystem.save_encrypted_file("gatos","mp4","meu amor", "aaaa", 34, videos)
fileSystem.save_encrypted_file("bem","jpeg","meu amor", "aaaa", 34, fotos)


fileSystem.list_directories(arvore)
fileSystem.decrypt_file(videos,"gatos")
print('-----------------')
fileSystem.list_files(media)
fileSystem.decrypt_file(root,"amor")



fileSystem.list_files(root)
print()
fileSystem.search_file(arvore,"artigo")

if __name__ == '__main__':

    fileSystem = FileSystem ()
    root = Directory ( "root" )
    docs = Directory ( "docs" )
    media = Directory ( "media" )
    tcc = Directory ( "tcc" )
    fotos = Directory ( "fotos" )
    videos = Directory ( "videos" )

    dirRoot = No ( root )
    dirDocs = No ( docs )
    dirMedia = No ( media )
    dirTcc = No ( tcc )
    dirFotos = No ( fotos )
    dirVideos = No ( videos )

    dirRoot.esquerda = dirDocs
    dirRoot.direita = dirMedia
    dirDocs.direita = dirTcc
    dirMedia.direita = dirFotos
    dirMedia.esquerda = dirVideos

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    arvore = ArvoreAVL ( dirRoot )
    
    print ( fileSystem.menu () )
    key = input ( 'Choice Password: ' )
    fileSystem.generate_encryption_key ( key )
    while True:

        print ( fileSystem.menu () )

        option = input ( "Select an option: " )

        if option == "1":
            fileSystem.list_directories ( arvore )
            time.sleep ( 4 )

        elif option == '2':
            key = input ( 'Password: ' )
            fileSystem.revoke_encryption_key ( key )

        elif option == "3":
            arquive_name = input ( 'Arquive Name: ' )
            t = input ( 'Arquive Type: ' )
            description = input ( 'Description: ' )
            size = input ( 'size: ' )
            content = input ( 'content: ' )
            directory = input ( 'directory: ' )
            if directory == 'docs':
                fileSystem.save_encrypted_file ( arquive_name, t, description, size, content, docs )
            elif directory == 'tcc':
                fileSystem.save_encrypted_file ( arquive_name, t, description, size, content, tcc )
            elif directory == 'root':
                fileSystem.save_encrypted_file ( arquive_name, t, description, size, content, root )
            elif directory == 'fotos':
                fileSystem.save_encrypted_file ( arquive_name, t, description, size, content, fotos )
            elif directory == 'videos':
                fileSystem.save_encrypted_file ( arquive_name, t, description, size, content, videos )
            elif directory == 'media':
                fileSystem.save_encrypted_file ( arquive_name, t, description, size, content, media )
            else:
                print ( 'Choose an existing directory!' )

        elif option == "4":

            directory = input ( ' Insert a directory: ' )

            if directory == 'Docs':
                fileSystem.list_files ( docs )
            elif directory == 'tcc':
                fileSystem.list_files ( tcc )
            elif directory == 'root':
                fileSystem.list_files ( root )
            elif directory == 'fotos':
                fileSystem.list_files ( fotos )
            elif directory == 'videos':
                fileSystem.list_files ( videos )
            elif directory == 'media':
                fileSystem.list_files ( media )
            else:
                assert directory, 'Choose an existing directory!'



        elif option == "5":
            directory = input ( 'Insert a directory: ' )
            assert type ( directory ) == type ( directory ), 'It needs to be of type directory.'
            Arquive = input ( 'Enter a file name: ' )


            if directory == 'docs':
                fileSystem.decrypt_file( docs, Arquive )
            elif directory == 'tcc':
                fileSystem.decrypt_file ( tcc, Arquive )
            elif directory == 'root':
                fileSystem.decrypt_file ( root, Arquive )
            elif directory == 'fotos':
                fileSystem.decrypt_file ( fotos, Arquive )
            elif directory == 'videos':
                fileSystem.decrypt_file ( videos, Arquive )
            elif directory == 'media':
                fileSystem.decrypt_file ( media, Arquive )
            else:
                assert directory, 'Choose an existing directory!'

        elif option == "6":
            key_word = input ( ' key_word: ' )
            fileSystem.search_file ( arvore, key_word )

        elif option == '10':
            print('                closing Program....')
            time.sleep(4)
            break

        else:
            print ( "Invalid option. Please try again." )
            time.sleep ( 4 )

