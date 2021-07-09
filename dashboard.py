import webbrowser
import shutil
import pathlib
import os


path = str(pathlib.Path().resolve())

def verificaExistenciaArquivo(nomeArquivo):
    path = str(pathlib.Path().resolve())+"/web/"+nomeArquivo
    fileObj = pathlib.Path(path)

    return pathlib.Path.exists(fileObj)



def moveTabelas():
    shutil.move(path+"/tabela.html",path+"/web")
    shutil.move(path+"/tabela_valortotal.html",path+"/web")
    shutil.move(path+"/tabelaConfiguracoes.html",path+"/web")

def deletaTabelasAntigas():
    if verificaExistenciaArquivo("tabela.html"):
        os.remove(path+"/web/tabela.html")

    if verificaExistenciaArquivo("tabela_valortotal.html"):
        os.remove(path+"/web/tabela_valortotal.html")

    if verificaExistenciaArquivo("tabelaConfiguracoes.html"):
        os.remove(path+"/web/tabelaConfiguracoes.html")

def abreDashboard():
    deletaTabelasAntigas()
    moveTabelas()
    webbrowser.open(path+"/web/lista.html",new=1)


