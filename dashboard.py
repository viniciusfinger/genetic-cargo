import webbrowser
import shutil
import pathlib
import os


path = str(pathlib.Path().resolve())

def moveTabelas():
    shutil.move(path+"/tabela.html",path+"/web")
    shutil.move(path+"/tabela_valortotal.html",path+"/web")
    shutil.move(path+"/tabelaConfiguracoes.html",path+"/web")

def deletaTabelasAntigas():
    os.remove(path+"/web/tabela.html")
    os.remove(path+"/web/tabela_valortotal.html")
    os.remove(path+"/web/tabelaConfiguracoes.html")

def abreDashboard():
    deletaTabelasAntigas()
    moveTabelas()
    print("file://"+path+"/lista.html")
    webbrowser.open(path+"/web/lista.html",new=1)
