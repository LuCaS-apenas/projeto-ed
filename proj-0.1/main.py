from AVLTree import *
from directory import *
from encryptionKey import *
from file import *
from fileSystem import *
import cryptocode


def add_dir(name):
    new = Directory(name)
    newDir = No(new)
    return newDir





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
fileSystem.list_files(media)
fileSystem.decrypt_file(root,"amor")

fileSystem.list_files(root)
print()
fileSystem.search_file(arvore,"artigo")







